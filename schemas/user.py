from pydantic import BaseModel, Field
import datetime

class User(BaseModel):
    name: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    email: str
    username: str
    password: str
    cohabitation_agreement: bool
    hashed_password: str
    status: int
    description: str
    knowledge_interests: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    forgot_password: bool
    image_profile: str
    phone_number: str
    class Config:
        orm_mode=True
        schema_extra = {
            "example": {
                "name": "edwin",
                "lastname": "hernandez",
                "email": "edwin.jhnsn@gmail.com",
                "username": "edwinjhs",
                "password": "12345678",
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
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username:str
