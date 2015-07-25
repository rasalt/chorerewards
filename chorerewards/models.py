import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from flask.ext.login import UserMixin

from .database import Base, engine

class Chore(Base):
  __tablename__ = "chores"
  id = Column(Integer, primary_key=True)
  title = Column(String(1024))
  content = Column(Text)
  datetime = Column(DateTime, default=datetime.datetime.now)


class User(Base, UserMixin):
  __tablename__ = "users"
  id = Column(Integer, primary_key=True)
  name = Column(String(1024))
  role = Column(String(1024))
  familyname = Column(String(1024))
  emailaddr  = Column(String(128), unique = True)
  passwd = Column(String(1024))
  
class Award(Base):
  __tablename__ = "awards"
  id = Column(Integer, primary_key=True)


class ChoreAssignment(Base):
  __tablename__ = "choreassignments"
  id = Column(Integer, primary_key=True)
    

class AwardRequest(Base):
  __tablename__ = "awardrequests"
  id = Column(Integer, primary_key=True)
    
class Rating(Base):
  __tablename__ = "ratings"
  id = Column(Integer, primary_key=True)
    

Base.metadata.create_all(engine)