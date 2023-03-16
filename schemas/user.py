from pydantic import BaseModel, Field
import datetime

class User(BaseModel):
    name: str = Field(min_length=1)
    lastname: str = Field(min_length=1)
    email: str
    username: str
    password: str
    cohabitation_agreement: bool
    status: int
    description: str
    knowledge_interests: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    forgot_password: bool
    image_profile: str
    phone_number: str
    class Config:
        schema_extra = {
            "example": {
                "name": "edwin",
                "lastname": "hernandez",
                "email": "edwin.jhnsn@gmail.com",
                "username": "edwinjhs",
                "password": "12345678",
                "cohabitation_agreement": True,
                "status": 0,
                "description": "backend iasdas",
                "knowledge_interests": "conocimiento, etc",
                "created_at": "2023-03-08T15:40:10",
                "updated_at": "2023-03-08T15:40:10",
                "forgot_password": False,
                "image_profile": "../image/profile1.jpg",
                "phone_number": "3213943876"
            }
        }