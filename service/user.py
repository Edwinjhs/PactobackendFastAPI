from fastapi import FastAPI, HTTPException, Depends, status
from models.user import Users as UserModel
from sqlalchemy.orm import Session

# HASHING AND JWT 
from jose import JWTError, jwt
from passlib.context import CryptContext

from schemas.user import User as UserSchema
from database import SessionLocal
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt


class UserService():
    pwd_context = CryptContext(schemes=[bcrypt], deprecated="auto")
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def __init__(self, db: Session):
        if not isinstance(db, Session):
            raise TypeError("db must be a Session instance")
        self.db = db

    def get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close


# auth
    def get_users(self):
        result = self.db.query(UserModel).all()
        return result
    
    def create_user(self, user:UserSchema):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        user_model = UserModel(
        name = user.name,
        lastname = user.lastname,
        email = user.email,
        username = user.username,
        password = hashed_password,
        cohabitation_agreement = user.cohabitation_agreement,
        status = user.status,
        description = user.description,
        knowledge_interests = user.knowledge_interests,
        created_at = user.created_at,
        updated_at = user.updated_at,
        forgot_password = user.forgot_password,
        image_profile = user.image_profile,
        phone_number = user.phone_number
        )
        self.db.add(user_model)
        self.db.commit()
        return
    
    def get_user_by_id(self,id:int):
        result = self.db.query(UserModel).filter(UserModel.id == id).first()
        return result
    
    def delete_user(self,id:int):
        user = self.get_user_by_id(id)
        if not user:
            return None
        self.db.delete(user)
        self.db.commit()
        return user

    def get_user_by_username(self, username: str):
        user_model = self.db.query(UserModel).filter(UserModel.username == username).first()
        if user_model is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Username {username} does not exist"
            )
        return user_model
    
    def update_user(self,id:int, user_schema:UserSchema):
        user = self.db.query(UserModel).get(id)
        if user:
            user.name=user_schema.name
            user.lastname = user_schema.lastname
            user.email = user_schema.email
            user.username = user_schema.username
            user.password = user_schema.password
            user.cohabitation_agreement = user_schema.cohabitation_agreement
            user.status = user_schema.status
            user.description = user_schema.description
            user.knowledge_interests = user_schema.knowledge_interests
            user.created_at = user_schema.created_at
            user.updated_at = user_schema.updated_at
            user.forgot_password = user_schema.forgot_password
            user.image_profile = user_schema.image_profile
            user.phone_number = user_schema.phone_number
            self.db.commit()
            return True
        return False
    
