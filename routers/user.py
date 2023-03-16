from fastapi import APIRouter, Depends
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import session, Session

from service.user import UserService as UserService
from schemas.user import User as UserSchema
from service.token import user_token as TokenService

user_router = APIRouter()

@user_router.get("/api/",tags=['user'])
def read_api(db: session = Depends(UserService.get_db)):
    result = UserService(db).get_users()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@user_router.post("/api/",tags=['user'],status_code=201,response_model=dict)
def create_user(user:UserSchema,db: session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    UserService(db).create_user(user)
    return JSONResponse(content={"message":"Se ha registrado un user","status_code":201})


@user_router.delete('/api/user/{id}',tags=['user'])
def delete_user(id:int, db: session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    success = UserService(db).delete_user(id)
    if success:
        return JSONResponse(status_code=202,content={"message":"User deleted"})
    else:
        return JSONResponse(content="user not found", status_code=404)

@user_router.get("/api/user/{username}",tags=['user'])
def get_user_by_username(username, db: Session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    user = UserService(db).get_user_by_username(username)
    return user


@user_router.put('/api/user/{id}',tags=['user'])
def update_user(id:int,user:UserSchema, db: session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    result = UserService(db).update_user(id, user)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun user","status_code":"404"})
    UserService(db).update_user(id,user)
    return JSONResponse(content={"message":'Se ha modificado el user con id: {id}'})

