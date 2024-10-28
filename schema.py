
from pydantic import BaseModel
from typing import Optional

class task_schema(BaseModel):
   task_name :str
   task_des :str
   created_by : Optional[str]= None
   date_created : Optional[str]= None

class artist_schema(BaseModel):
   artist_name :str
   artist_firstname :str
   artist_lastname :str

class release_schema(BaseModel):
   release_title :str
   release_date :str
   release_artist :int

   class Config:
       orm_mode = True