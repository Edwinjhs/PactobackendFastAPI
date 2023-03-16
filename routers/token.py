from fastapi import  HTTPException, Depends,  APIRouter, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import bcrypt

import service.token as Token_service
from models.user import Users as UserModel
from service.user import UserService as UserService
from schemas.user import User as UserSchema
from service.token import user_token as TokenService

token_router = APIRouter()



@token_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(UserService.get_db)):
    user = TokenService.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    # si la contraseña y usuario coincide se crea el token y se le da el tiempo de expiracion
    access_token_expires = timedelta(minutes=Token_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = TokenService.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires)
    return{"access_token": access_token, "token_type": "bearer"}


@token_router.get("/api/users/me")
async def read_users_me(current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    return current_user
# obtiene el usuario actual

@token_router.get("/api/users/me/items/")
async def read_users_me_items(current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
# obtiene los items del usuario actual