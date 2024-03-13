from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, index=True, comment='user_id')
    email = Column(String, unique=True, index=True, comment='email')
    password = Column(String)
