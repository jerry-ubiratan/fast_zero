from http import HTTPStatus
from fastapi import FastAPI
from fast_zero.schemas import Message, UserSchema, UserPublicSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!!!!!!'}

@app.post('/users', status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_user(user: UserSchema):
    return {'message': 'User created successfully'} 