from sqlalchemy import Boolean, Column, Integer, String

from database import Base

class Login(Base):
    __tablename__ = "login"

    address = Column(String, primary_key=True, index=True)
    password = (String)