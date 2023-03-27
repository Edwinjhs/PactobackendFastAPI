from fastapi import APIRouter, Depends
from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import session, Session

from service.user import UserService as UserService
from schemas.user import User as UserSchema
from service.token import user_token as TokenService

# Creating an instance of the APIRouter class
user_router = APIRouter()

# Defining a GET route for getting all users
@user_router.get("/api/user/get",tags=['user'])
def read_api(db: session = Depends(UserService.get_db)):
    # Calling the get_users() method from the UserService class to retrieve all users
    result = UserService(db).get_users()
    # Returning a JSON response with the retrieved users
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

# Defining a POST route for creating a new user
@user_router.post("/api/user/post",tags=['user'],status_code=201,response_model=dict)
def create_user(user:UserSchema,db: session = Depends(UserService.get_db)):
    # Calling the create_user() method from the UserService class to create a new user
    UserService(db).create_user(user)
    # Returning a JSON response with a message indicating that the user has been created
    return JSONResponse(content={"message":'Se ha creado el usuario correctamente'})

# Defining a DELETE route for deleting a user by id
@user_router.delete('/api/user/delete/{id}',tags=['user'])
def delete_user(id:int, db: session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    success = UserService(db).delete_user(id)
    if success:
        return JSONResponse(status_code=202,content={"message":"User deleted"})
    else:
        return JSONResponse(content="user not found", status_code=404)

# Defining a GET route for getting a user by their username
@user_router.get("/api/user/get/{username}",tags=['user'])
def get_user_by_username(username, db: Session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    user = UserService(db).get_user_by_username(username)
    return user

# Defining a PUT route for updating a user by id
@user_router.put('/api/user/put/{id}',tags=['user'])
def update_user(id:int,user:UserSchema, db: session = Depends(UserService.get_db),current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    result = UserService(db).update_user(id, user)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun user","status_code":"404"})
    UserService(db).update_user(id,user)
    return JSONResponse(content={"message":"Se ha modificado el user con id: {id}"})

