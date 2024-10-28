from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base

class Task(Base):
   __tablename__ = "Tasks"
   id = Column(Integer, primary_key=True, index=True)
   task_name = Column(String(20))
   task_des = Column(Text())
   created_by = Column(String(20))
   date_created = Column(String(15))

class Artist(Base):
   __tablename__ = "Artists"
   id = Column(Integer, primary_key=True, index=True)
   artist_name = Column(String(255))
   artist_firstname = Column(String(255))
   artist_lastname = Column(String(255))

class Release(Base):
   __tablename__ = "Releases"
   id = Column(Integer, primary_key=True, index=True)
   release_title = Column(String(255))
   release_date = Column(String(15))
   release_artist = Column(Integer)