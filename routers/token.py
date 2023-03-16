from fastapi import  HTTPException, Depends,  APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
import bcrypt

from models.user import Users as UserModel
from service.user import UserService as UserService
from schemas.user import User as UserSchema
from service.token import user_token as TokenService

token_router = APIRouter()

@token_router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: session = Depends(UserService.get_db)):
    user = db.query(UserModel).filter(UserModel.username == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if not bcrypt.checkpw(form_data.password.encode('utf-8'), user.password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "Bearer"}


@token_router.get("/api/users/me")
async def read_users_me(current_user: UserSchema = Depends(TokenService.get_current_active_user)):
    return current_user
