from fastapi import FastAPI, Path
from enum import Enum

class UserType(str, Enum):
    STANDAR : 'standar'
    ADMIN : 'admin'

app = FastAPI()


@app.get('/')
async def hellow_world():
    return {'hellow word'}

@app.get('/users/{id}')
async def get_user(id: int = Path(..., ge=1)):
    return {'id':id}

@app.get("/users/{type}/{id}")
async def get_user(type: UserType, id: int):
    return {"type": type, "id": id}

@app.get('/license-plates/{license}')
async def get_license_plate(license : str = Path(..., regex=r'^7\w{2}-\d{3}-\w{2}$')):
    return {'license':license}

# @app.get('/users/{type}/{id}')
# async def get_user_t(type: str, id: int):
#     return {'type':type, 'id':id}
