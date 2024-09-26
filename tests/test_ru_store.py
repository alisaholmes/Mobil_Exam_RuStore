import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag('Mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Alisa Holmes')
@allure.feature('Мобильное тестирование приложения "RuStore"')
@allure.story('Тестирование онбординга в приложении "RuStore"')
def test_verify_onboarding_screen():
    with allure.step('Прохождение экрана онбординга'):
        browser.element((AppiumBy.ID, 'ru.vk.store:id/action_bar_root')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Продолжить')).click()
    with allure.step('Проверяем видимость рекламного блока с рекомендациями'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().resourceId("START_RECOMMENDATION_ADVERTISEMENT_BLOCK_TAG")')).should(
            be.visible)


@allure.tag('Mobile')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'Alisa Holmes')
@allure.feature('Мобильное тестирование приложения "RuStore"')
@allure.story('Прохождение экрана рекомендаций и настройка уведомлений "RuStore"')
def test_recommendations():
    with allure.step('Прохождение экрана онбординга'):
        browser.element((AppiumBy.ID, 'ru.vk.store:id/action_bar_root')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Продолжить')).click()
    with allure.step('Выбираем чекбоксы'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("BADGE_COMPONENT_TEST_TAG").instance(2)')).click()
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("BADGE_COMPONENT_TEST_TAG").instance(1)')).click()
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().resourceId("BADGE_COMPONENT_TEST_TAG").instance(0)')).click()
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().resourceId("BADGE_COMPONENT_TEST_TAG").instance(3)')).click()
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR,
                         'new UiSelector().resourceId("APP_ICON_COMPONENT_TEST_TAG").instance(4)')).click()

    with allure.step('Нажимаем "Скачать все"'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                       '"START_RECOMMENDATION_DOWNLOAD_BUTTON_TAG")')).click()
    with allure.step('Нажимаем "Don t allow"'):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()


@allure.tag('Mobile')
@allure.severity(Severity.MINOR)
@allure.label('owner', 'Alisa Holmes')
@allure.feature('Мобильное тестирование приложения "RuStore"')
@allure.story('Проверка информации о компании и ИНН "RuStore"')
def test_name_and_inn_of_the_company():
    with allure.step('Прохождение экрана онбординга'):
        browser.element((AppiumBy.ID, 'ru.vk.store:id/action_bar_root')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Продолжить')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Реклама • 18+')).click()
    with allure.step('Проверка текста'):
        browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId('
                                                       '"START_RECOMMENDATION_ADVERTISEMENT_DESCRIPTION_TAG")')).should(
            have.text('ООО "ВК", ИНН 7743001840'))
