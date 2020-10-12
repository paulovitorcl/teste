from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"Desafio Técnico":"Stone"}

#Criando a base model
class Usuario(BaseModel):
    nome: str
    sobrenome: str
    CPF: str
    email: str
    data: str


# Criando uma base de dados inicial

base_de_dados = [
    Usuario(nome="Paulo Vitor", sobrenome="Costa Lima", CPF="066.880.055-55", email="pvcl1996@hotmail.com", data="15/10/1996"),
    Usuario(nome="João", sobrenome="Silva", CPF="088.880.177-55", email="joao.silva@hotmail.com", data="23/08/1998"),
    Usuario(nome="Maria", sobrenome="Santos", CPF="112.880.055-55", email="marina_sts@hotmail.com", data="14/01/2000")
]

# Rota que retorna todos os Usuários
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota que procura um usuário pelo CPF 
@app.get("/usuarios/{CPF_usuario}")
def get_usuario_cpf(CPF_usuario: str):
    for usuario in base_de_dados:
        if(usuario.CPF == CPF_usuario):
            return usuario

    return {"Status": 404, "Mensagem": "Não encontrou nenhum usuário com este CPF"}
