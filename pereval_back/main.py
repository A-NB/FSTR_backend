import os

from typing import Optional, List

from xmlrpc.client import DateTime

from fastapi import FastAPI

from models import Data, User, Level, Coords

app = FastAPI()

host_server = os.environ.get('host_server', 'localhost')
db_port = str(os.environ.get('FSTR_DB_PORT', '5432')) #u rllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
db_host = os.environ.get('FSTR_DB_HOST', 'pereval')
db_login = str(os.environ.get('FSTR_DB_LOGIN', 'postgres')) # urllib.parse.quote_plus(str(os.environ.get('FSTR_DB_LOGIN', 'postgres')))
db_pass = str(os.environ.get('FSTR_DB_PASS', 'secret')) # urllib.parse.quote_plus(str(os.environ.get('FSTR_DB_PASS', 'secret')))
## ssl_mode = str(os.environ.get('ssl_mode','prefer')) # urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_login, db_pass, host_server, db_port, db_host) #, ssl_mode)

d = DateTime

db: Data = {
    "id": "25",
    "beautyTitle": "Beauty",
    "title": "Перевал",
    "other_titles": "Хрень",
    "connect": "Some", #что соединяет  
    "add_time": d,
    "user": {
        "id": "25",
        "email": "1@1.ru",
        "phone": "12345678912",
        "fam": "Pup",
        "name": "Vasya",
        "otc": ""
        },
    "coords": {
        "latitude": "45.3842",
        "longitude": "7.1525",
        "height": "1200"
        },
    "type": "pass", # константа для всех запросов приложения 
    "level": {
        "winter": "", # текстовое поле "Категория трудности"
        "summer": "1А",
        "autumn": "1А",
        "spring": ""
        },
    "images": [
        {"url":"http://...", "title":"Подъём. Фото №2"},
        {"url":"http://...", "title":"Седловина"},
        {"url":"http://...", "title":"Спуск. Фото №99"}
        ],
    "status": "new" # Внимание участникам! Поправка в БД: добавьте поле status как отдельную колонку в базу данных, тип данных varchar(20).
    }


@app.get("/")
async def read_root():
    return {"Hello": "Андрей"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/submitData")
async def add_data(data: Data):
    try:
        db.append(data)
    except:
        ...
    finally:
        ...
    return {"status": "status", "message": "message"}


@app.get("/submitData/:id/status") #GET /submitData/:id/status — получить статус модерации отправленных данных.
async def get_moderation_status():
    return


@app.post("/submitData/:id") #PUT /submitData/:id — отредактировать существующую запись (замена), если она в статусе new. Редактировать можно все поля, кроме ФИО, почта, телефон.
async def modify_data():
    return


@app.get("/submitData/") #GET /submitData/ — список всех данных для отображения, которые этот пользователь отправил на сервер через приложение с возможностью фильтрации по данным пользователя (ФИО, телефон, почта), если передан объект.
async def get_moderation_status():
    return        


@app.get("/submitData/:id") #GET /submitData/:id — получить одну запись (перевал) по её id. При создании записи в БД, бэк возвращает фронту id и фронт этот id сохраняет у себя локально. За счёт этого может редактировать записи, которые ещё не отрезолвлены модератором.
async def get_moderation_status():
    return



# ВАЖНО: путь к базе данных, а также логин и пароль нужно получать из переменных окружения. Нужно использовать следующие переменные окружения:
#         FSTR_DB_HOST: путь к базе данных                      
#         FSTR_DB_PORT: порт базы данных                        5432
#         FSTR_DB_LOGIN: логин, с которым вы подключаетесь к БД
#         FSTR_DB_PASS: пароль, с которым вы подключаетесь к БД

# Ваше REST API должно заполнять табличку pereval_added. При добавлении нового перевала в таблицу вы в поле status ставите значение new. После этого с табличкой будет работать внешнее приложение, и изменять значение этого поля. 

# Допустимые значения поля status:

#         new;
#         pending — если модератор взял в работу;
#         resolved — модерация прошла успешно;
#         accepted — более информативные вариации resolved;
#         rejected — более информативные вариации resolved.




# В MVP 2 пользователь может выполнять следующие действия:

#         Редактировать отправленные на сервер данные об объекте, если они в статусе new. Редактировать можно все поля, кроме ФИО, почта, телефон. После модерации данные менять нельзя.
#         Просматривать статус модерации.
#         Просматривать все объекты, которые пользователь сам отправлял когда-либо на сервер, и их статусы.

# Операции API для MVP2:

# MVP 2 должно поддерживать следующие операции:

#         GET /submitData/:id/status — получить статус модерации отправленных данных.
#         PUT /submitData/:id — отредактировать существующую запись (замена), если она в статусе new. Редактировать можно все поля, кроме ФИО, почта, телефон.
#         GET /submitData/ — список всех данных для отображения, которые этот пользователь отправил на сервер через приложение с возможностью фильтрации по данным пользователя (ФИО, телефон, почта), если передан объект.
#         GET /submitData/:id — получить одну запись (перевал) по её id. При создании записи в БД, бэк возвращает фронту id и фронт этот id сохраняет у себя локально. За счёт этого может редактировать записи, которые ещё не отрезолвлены модератором.
