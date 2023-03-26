from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime,ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    id_type_actor= Column(Integer, ForeignKey("type_actor.id"))
    id_city = Column(Integer, ForeignKey("city.id"))
    id_contribution= Column(Integer, ForeignKey("contribution.id"))
    name_user = Column(String)
    lastname = Column(String)
    email = Column(String)
    username = Column(String)
    password = Column(String)
    entidad = Column(String)
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

    type_actor_U = relationship("TypeActor", back_populates="user_TA")

    contribution = relationship('Contribution', back_populates='users')