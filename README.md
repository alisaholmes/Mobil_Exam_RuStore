# Дипломный проект по мобильному тестированию приложения "RuStore"

### [Ссылка на сайт магазина приложений](https://www.rustore.ru/)
![This is an image](design/images/rustore_deeplink.jpg)


## Содержание
- [Технологии и инструменты](#технологии-и-инструменты)
- [Список проверок](#список-проверок)
- [Настройка тестового стенда в режимах эмулятора и реального устройства](#настройка-тестового-стенда-в-режимах-эмулятора-и-реального-устройства)
- [Локальный запуск тестов и получение отчета](#локальный-запуск-тестов-и-получение-отчета)
- [Отчет в Allure-reports](#отчет-в-allure-reports)
- [Видео запуска тестов на эмуляторе](#видео-запуска-тестов-на-эмуляторе)




## Технологии и инструменты
Проект реализован с использованием Python, PyCharm, Pytest, Appium, Android Studio, Allure Report.
<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40"/>
<img src="design/icons/Appium_pic.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/androidstudio/androidstudio-original.svg" height="40" width="40"/>
<img src="design/icons/Allure_Report.svg" height="40" width="40"/>  
     


## Список проверок

- [x] Тестирование онбординга в приложении "RuStore"
- [x] Прохождение экрана рекомендаций и настройка уведомлений "RuStore"
- [x] Проверка информации о компании и ИНН "RuStore"

## Настройка тестового стенда в режимах эмулятора и реального устройства

Отдельное руководство по установке Appium, Android Studio и созданию эмулятора мобильного устройства можно найти в интернете. Ниже приведена инструкция по запуску тестового окружения для проведения локальных тестов на эмуляторе и реальном устройстве.

### Настройка окружения для эмулятора

<details><summary>1. Запуск Appium сервера</summary>
Для запуска Appium необходимо открыть командную строку и выполнить следующую команду:

```
appium --base-path "/wd/hub"
```
</details>

<details><summary>2. Запуск виртуального устройства</summary>
Для того чтобы запустить виртуальное устройство, необходимо открыть Android Studio и на странице Device Manager в строке с созданным устройством нажать на кнопку "Play"

![This is an image](design/images/1.png)

![This is an image](design/images/3.png)

</details>

### Настройка окружения для реального устройства
<details><summary>1. Подготовка реального устройства к подключению</summary>

 - Перейти в настройки устройства;
 - Открыть пункт `О телефоне`;
 - Нажать на пункт Номер сборки несколько раз, пока не появится сообщение о том, что режим разработчика активирован;
 - Перейти в настройки разработчика;
 - Активировать режим разработчика;
 - Активировать отладку по USB.
 - Подключить устройство к компьютеру через USB-кабель.
 - При первом подключении устройства к компьютеру необходимо дать разрешение на подключение к компьютеру, выбрав пункт `Всегда разрешать....`
 - После подключения устройства проверить его отображение с помощью команды`adb devices`.

</details>

<details><summary>1. Запуск Appium сервера </summary>

Для запуска Appium необходимо открыть командную строку и выполнить следующую команду:

```
appium --base-path "/wd/hub"
```
</details>

## Локальный запуск тестов и получение отчета

<details><summary>1. Склонировать репозиторий</summary>

```
git clone git@github.com:alisaholmes/Mobil_Exam_RuStore.git
```
</details>


<details><summary>2. Создать и активировать виртуальное окружение, установить зависимости и запустить тесты через эмулятор</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest --context=local_emulator # команда запуска на эмуляторе
pytest --context=local_real_device # запуск теста на реальном устройстве
```
</details>

<details><summary>3. Сформировать отчет о прохождении тестов в allure</summary>

```
allure serve allure-results
```
Или 

```
allure generate
```
</details>

 После выполнения команды в проекте появится папка allure-report или автоматически откроется браузер с Allure-отчетом

## Отчет в Allure-reports

<details><summary>Отчет о результатах тестирования в Allure-reports</summary>

<img src="design/images/allure_1.png">

</details>
<details><summary>Тесты</summary>

<img src="design/images/allure_2.png">

</details>


## Видео запуска тестов на эмуляторе

<p align="center">
<img src="design/images/test.gif">
</p>