# Telegram_space 
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

___
#### Это telegram bot который оправляет фотографии космоса.
___
>### Для запуска программы требуется:
 * скачать [Python](https://www.python.org/) версии 3.1 или выше.
 * операционная система macOS, linux, windows 7 или выше.
 * установить все нужные библиотеки Python командой:
```
pip install -r requirements.txt
```
___
>### Переменные окружения:
 * `API_NASA` - ваш API токен `NASA`.
 * `ID_LAUNCH` - ваш ID запуска ракеты `SpaceX`.
 * `API_BOT` - API `telegram бота` которого вы создадите в telegram.
 * `CHAT_ID` - ID чата в которого будут отправляться фотографии.
 * `TIME_SLEEP` - время отправки между фотографий.
___
>### Как запустить программу:

* Прежде чем запустить программу нужно скачать фотографии с помощью кода, либо добавить свои фотографии.

* Как скачать фотографии NASA:
    * В консоли пишем команду:
    ```
    python fetch_nasa.py
    ```
* Как скачать фотографии SpaceX:
    * В консоли пишем команду:
    ```
    python fetch_spacex_launch.py id_launch
    ```
    * id_launch - это ваш `ID` запуска SpaceX :rocket:.
    * По умолчанию `id_launch` уже записан.
* Как скачать фотографии EPIC:
    * В консоли пишем команду:
    ```
    python fetch_epic_image.py
    ```
* Как только скачали, либо добавили фотографии запускаем основную программу.
    ```
    python telegram_bot.py time_sleep
    ```
    * `time_sleep` - время отправки между фотографиями. По умолчанию время стоит 4 часа, но вы можете поставить и своё время.`(время выстовляется в секндах)`.
___
>### Как работать с Dockerfile:

* Для того чтобы запустить, `Dockerfile` на своем компьютере, вам потребуется установить [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Далее запустите программу `Docker Dosktop`.
* После запуска `Docker Desktop`, в консоле напишите команду:
```
docker build -t telegram_space .
``` 
* `telegram_space` - название вашего образа
* `.` - путь до `Dockerfile`
* Далее в вашем `Docker Desktop` добавиться образ
![docker_image](picture/docker_image.png)
* После, вам требуется запустить этот образ. В консоле напишите команду:
```
docker run telegram_space
```
* `telegram_space` - название вашего образа который вы создавали ранее.
* После образ соберется в контейнер и бот будет запущен.
![docker_container](picture/docker_container.png)

>### Цель проекта:
* Код написан в образовательных целях 