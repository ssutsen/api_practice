from sqlalchemy import Boolean, Column, Integer, String

from database import Base

class Login(Base):
    __tablename__ = "login"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    password = Column(String)