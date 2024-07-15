from pydantic import BaseModel

class Message(BaseModel):
    message: str 

class UserPublicSchema(BaseModel):
    name: str
    email: str

class UserSchema(BaseModel):
    name: str
    email: str
    password: str
