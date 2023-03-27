from pydantic import BaseModel, Field
from typing import Optional
import datetime

class User(BaseModel):
    name_user: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    email: Optional[str] = None
    username: str
    password: str
    entidad: Optional[str] = None
    cohabitation_agreement: Optional[bool] = None
    hashed_password: Optional[str] = None
    status: int = 0
    description: Optional[str] = None
    knowledge_interests: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    forgot_password: bool = False
    image_profile: Optional[str] = None
    phone_number: Optional[str] = None
    class Config:
        # Allows using ORM mode to read from the database
        orm_mode=True
        # Defines an example schema for the User model
        schema_extra = {
            "example": {
                "name_user": "edwin",
                "lastname": "hernandez",
                "email": "edwin.jhnsn@gmail.com",
                "username": "edwinjhs",
                "password": "12345678",
                "entidad": "colegio monseñor",
                "hashed_password": "",
                "cohabitation_agreement": True,
                "status": 0,
                "description": "backend iasdas",
                "knowledge_interests": "conocimiento, etc",
                "forgot_password": False,
                "image_profile": "../image/profile1.jpg",
                "phone_number": "3213943876"
            }
        }
class Token(BaseModel):
    # JWT access token
    access_token: str
    # Type of token (usually "bearer")
    token_type: str

class TokenData(BaseModel):
    # Username associated with the token
    username:str
