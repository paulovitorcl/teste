from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {"Stone DevOps | SRE Challenge":"Paulo Vitor Costa Lima"}

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
    Usuario(nome="Maria", sobrenome="Santos", CPF="112.880.055-55", email="marina_sts@hotmail.com", data="14/01/2000"),
    Usuario(nome="Antônio", sobrenome="Costa", CPF="332.873.775-45", email="antonio_costa@gmail.com", data="11/11/1992"),
    Usuario(nome="Jeferson", sobrenome="Silveira", CPF="998.992.342-72", email="j.silveira@gmail.com", data="18/03/1999"),
    Usuario(nome="Carla", sobrenome="Bueno", CPF="112.987.332-43", email="carla-bueno@hotmail.com", data="27/09/1994"),
    Usuario(nome="Juliana", sobrenome="Moraes", CPF="222.991.564-32", email="moraes_ju@yahoo.com.br", data="30/03/1996")
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


# Rota que insere um Usuário
@app.post("/usuarios/inserir_usuario")
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario) 
    return usuario
