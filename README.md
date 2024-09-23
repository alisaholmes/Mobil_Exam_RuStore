# Дипломный проект по мобильному тестированию приложения "RuStore"


## Содержание
- [Технологии и инструменты](#технологии-и-инструменты)
- [Список проверок](#cписок-проверок)
- [Локальный запуск тестов и получение отчета](#локальный-запуск-тестов-и-получение-отчета)
- [Отчет о результатах тестирования в Allure-reports](#отчет-о-результатах-тестирования-в-allure-reports-)
- [Автоматическое оповещение о результатах сборки Jenkins в Telegram-бот](#автоматическое-оповещение-о-результатах-сборки-jenkins-в-telegram-бот)



## Технологии и инструменты
Проект реализован с использованием Python, PyCharm, Pytest, Appium, Android Studio, Allure Report, Jenkins, Allure TestOps, Telegram.
<p align="left">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" height="40" width="40"/>
<img src="design/icons/Appium_pic.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/androidstudio/androidstudio-original.svg" height="40" width="40"/>
<img src="design/icons/Allure_Report.svg" height="40" width="40"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40"/>      
<img src="design/icons/allure_testops.svg" height="40" width="40"/>     
<img src="design/icons/telegram.png" height="40" width="40"/>     


## Список проверок

- [x] Тестирование онбординга в приложении "RuStore"
- [x] Прохождение экрана рекомендаций и настройка уведомлений "RuStore"
- [x] Проверка информации о компании и ИНН "RuStore"

 

## Локальный запуск тестов и получение отчета

<details><summary>1. Склонировать репозиторий</summary>

```
git clone git@github.com:alisaholmes/Mobil_Exam_RuStore.git
```
</details>


<details><summary>2. Создать и активировать виртуальное окружение, установить зависимости и запустить тесты</summary>

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . || true
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

<details><summary>4. После выполнения команды откроется браузер с отчетом</summary>

## <img src="design/icons/Allure_Report.svg" height="40" width="40"/> Отчет в Allure report</a></a>

<details><summary>Отчет о результатах тестирования в Allure-reports</summary>

<img src="design/images/allure_1.png">

</details>
<details><summary>Тесты</summary>

<img src="design/images/allure_2.png">

</details>

## Автоматическое оповещение о результатах сборки Jenkins в Telegram-бот

![This is an image](design/images/tele.png)