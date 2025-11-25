from fastapi import FastAPI
from fastapi import HTTPException
from erros import *
from service.service import ElencoService
app=FastAPI()

service=ElencoService()


##
# aqui seria o controler 
# #

@app.get("/")
def home():
    return "ola mano"
@app.get("/elenco")
def elenco():
    return service.retornar_elenco()
@app.get("/busca/")
def busca_com_filtro(status:bool=True,habilidade:str=None,mais_votado:bool=False):
    try:
        dados=service.buscar_com_filtro(vivo=status,habilidade_=habilidade,mais_votado_=mais_votado)
    except ErroNenhumResultado:
        raise HTTPException(status_code=404, detail="nenhum personagem encontrado com essas caracteristicas")
    except ErroValidacao:
        raise HTTPException(status_code=404, detail="Erro ao validar os dados inseridos")
    except ErroSemParametros:
        raise HTTPException(status_code=404, detail="Nenhum parametro selecionado")
    except ErroValorMinimo:
        raise HTTPException(status_code=404, detail="o parametro habilidade nao tem o valor minimo")
    return dados
@app.get("/elenco/{ator}")
def busca_ator(ator:str):
    try:
        
        dados_ator=service.buscar_ator(nome=ator)

        return dados_ator
    except ErroValorMinimo:
        raise HTTPException(status_code=404, detail="Valor minimo de caracteres nao foram cumpridos")
    except ErroValidacao:
        raise HTTPException(status_code=404, detail="erro na validaçao dos dados inseridos")
    except ErroNenhumResultado:
        raise HTTPException(status_code=404, detail="ator nao enconstrado")
@app.get("/personagem/{personagem}")
def buscar_personagem(personagem:str):
    try:
        dados_personagem=service.buscar_personagem(nome=personagem)
        
        return dados_personagem
    except ErroValorMinimo:
        raise HTTPException(status_code=404, detail="Valor minimo de caracteres nao foram cumpridos")
    except ErroNenhumResultado:
        raise HTTPException(status_code=404, detail="personagem nao enconstrado")
    except ErroValidacao:
        raise HTTPException(status_code=404, detail="erro na validaçao dos dados inseridos")
@app.post("/votar/{personagem}")
def upvote(personagem):
    try:
        #voto=service(personagem)
        return "sucesso"
    except ErroNenhumResultado:
         raise HTTPException(status_code=404, detail="personagem não encontrado")
    except ValorVazio:
        raise  HTTPException(status_code=404, detail="personagem não encontrado")
#uvicorn main:app --reload
