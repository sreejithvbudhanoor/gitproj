# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://testuser:Test@123@localhost/testdb')
Session = sessionmaker(bind=engine)

Base = declarative_base()