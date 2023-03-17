from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.orm import relationship

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
    
    posts = relationship("Posts", back_populates="owner")

