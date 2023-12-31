from pydantic import BaseModel


class Todo(BaseModel):
    id:int
    item:str


class TodoItem(BaseModel):
    class Config:
        Schema_extra = {
            "Example":{
                "id": 1,
                "item": "Example schema!"
            }
        }