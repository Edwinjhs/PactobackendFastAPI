from fastapi import HTTPException, Depends, status
from sqlalchemy.orm import session
import os

from schemas.user import User as UserSchema
from service.user import UserService as UserService
from models.user import Users as UserModel


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


class UserInDB(UserSchema):
    hashed_password: str

class user_token():

    def get_user(username: str, db):
        user_model = db.query(UserModel).filter(UserModel.username == username).first()
        if user_model is not None:
            return user_model

    def decode_token(token, db):
        user = user_token.get_user(token, db)
        return user

    async def get_current_user(token = Depends(UserService.oauth2_scheme),  db: session = Depends(UserService.get_db)):
        user = user_token.decode_token(token, db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    
    async def get_current_active_user(current_user: UserSchema = Depends(get_current_user)):
        # una funcion que obtiene un usuario actual activo a partir del token
        if current_user.status == 10:
            raise HTTPException(status_code=400, detail="Inactive user")
        elif current_user.status == 5:
            raise HTTPException(status_code=400, detail="Usuario no validado por el Admin")
        return current_user
    
