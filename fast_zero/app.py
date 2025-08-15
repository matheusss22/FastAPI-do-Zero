from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI(title="Documentação FastAPI do zero")


@app.get(
    '/', 
    status_code=HTTPStatus.OK, 
    response_model=Message
)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.get(
    '/exercice-html', 
    status_code=HTTPStatus.OK, 
    response_class=HTMLResponse
)
def exercice_02():
    return """
    <html>
      <head>
        <title>Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
