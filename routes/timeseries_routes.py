from fastapi import APIRouter, Path
from enum import Enum
from cryptography.fernet import Fernet
from config.plugMariaDB import conn
from models.timeSeries import timeSeries
from schemas.timeSeries import TimeSeries, ExchageFX
from utils.get_data import insertData

from typing import List
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy import func, select

user = APIRouter()
key = Fernet.generate_key()
f = Fernet(key)

class UserType(str, Enum):
    STANDAR : 'standar'
    ADMIN : 'admin'

@user.get('/')
async def hellow_world():
    return {'hellow word'}

@user.get('/users/{id}')
async def get_user(id: int = Path(..., ge=1)):
    return {'id':id}

@user.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

@user.get('/license-plates/{license}')
async def get_license_plate(license : str = Path(..., regex=r'^7\w{2}-\d{3}-\w{2}$')):
    return {'license':license}

@user.get("/users_db/{val}",response_model=List[TimeSeries])
def get_user(val: str):
    result = conn.execute(timeSeries.select().where(timeSeries.c.from_symbol == val))
    return result

@user.post('/h')
def insert_info(data: ExchageFX):
    return insertData(data)

# @user.get('/users/{type}/{id}')
# async def get_user_t(type: str, id: int):
#     return {'type':type, 'id':id}
