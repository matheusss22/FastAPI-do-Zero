from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI(title='🚀 Documentação FastAPI 🚀')

# Criando um banco de dados de teste:
database = []


@app.get(
    name='Boas vindas',
    description='Retorna uma mensagem de boas vindas',
    path='/',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def read_root():
    """
    Operação de GET na rota raiz
    """
    return {'message': 'Hello World'}


@app.get(
    name='Listar usuários',
    description='Retorna uma lista dos usuários registrados no banco de dados',
    path='/users',
    status_code=HTTPStatus.OK,
    response_model=UserList,
)
def read_users():
    """
    Operação para listar todos os usuários da base de dados
    """
    return {'users': database}


@app.post(
    name='Criar usuário',
    description='Cria um usuário no banco de dados',
    path='/users',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
)
def create_user(user: UserSchema):
    """
    Operação para criar um usuário na base de dados
    """
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.put(
    name='Editar usuário',
    description='Edita um reistro de usuário no banco de dados',
    path='/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
)
def update_user(user_id: int, user: UserSchema):
    """
    Operação para alterar os dados de um usuário na base de dados
    """
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    name='Deletar usuário',
    description='Deleta um usuário do banco de dados',
    path='/users/{user_id}',
    status_code=HTTPStatus.OK,
    response_model=Message,
)
def delete_user(user_id: int):
    """
    Operação para deletar o usuário do banco de dados
    """
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )

    del database[user_id - 1]

    return {'message': 'User deleted'}
