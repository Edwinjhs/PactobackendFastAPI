from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    lastname = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    hashed_password = Column(String)
    cohabitation_agreement = Column(Boolean)
    status = Column(Integer)
    description = Column(Text)
    knowledge_interests = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    forgot_password = Column(Boolean)
    image_profile = Column(String)
    phone_number = Column(String)


# {
#   "name": "Edwin",
#   "lastname": "Hernández",
#   "email": "edwin@gmail.com",
#   "username": "edwinjhs2",
#   "password": "casa123",
#   "cohabitation_agreement": True,
#   "status": 0,
#   "description": "Esta es la descripción",
#   "knowledge_interests": "Mis intereses",
#   "created_at": "2023-03-14T11:02:36.595Z",
#   "updated_at": "2023-03-14T11:02:36.595Z",
#   "forgot_password": False,
#   "image_profile": "string",
#   "phone_number": "+351964702709"
# }

