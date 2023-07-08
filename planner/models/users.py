from pydantic import EmailStr,BaseModel
from typing import Optional,List
from events import Event


class User(BaseModel):
    email:EmailStr
    password:str
    events:Optional[List[Event]]

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email:EmailStr
    password:str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }