# django-orm-watching-storage: пульт охраны банка 

Учебная задача в рамках модуля "Знакомство с Django: ORM — Урок 1 и 2: Пульт охраны банка" для учебной платформы [dvmn.org](https://dvmn.org)


Проект реализует следующие задачи:

1. Подключение к БД для получения текущих данных по посетителям хранилища, а так историю посещений
2. Web-интерфейс охранника


# Подготовка к использованию

Для запуска необходимо следующее:
- Установленный Python 3
- Установлены зависимости командой: 
```
pip install -r requirements.txt
```
- создан и заполнен файл `.env` в корне проекта. Формат файла ниже: 
```text
# Django common section
DEBUG=TRUE
# Django Database section
DB_ENGINE=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
```


# Использование

Чтобы локально запустить web-сервер, воспользуйтесь командой 
```
python manage.py runserver 0.0.0.0:8000
```

После запуска web-интерфейс будет доступен по адресу, указанному в командной строке.
Для 0.0.0.0:8000 этот адрес будет [следующим.](http://127.0.0.1:8000/) 

Главная страница будет отображать активные карты доступа посетителей и сотрудников банка.

