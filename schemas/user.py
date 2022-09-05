from pydantic import BaseModel

class User(BaseModel):
    nom:str
    email:str
    password:str