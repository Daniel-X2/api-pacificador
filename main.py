from fastapi import FastAPI
from fastapi import HTTPException
import json
from banco import banco

app=FastAPI()

db=banco()
@app.get("/")
def home():
    return "ola mano"
    
@app.get("/elenco")
def elenco():
    
    return db.elenco()
@app.get("/elenco/{nome}")
def busca_ator(nome:str):
    ator=db.buscar(nome)
    if ator:
        return ator
    raise HTTPException(status_code=404, detail="Ator não encontrado")
@app.get("/personagem/{nome}")
def buscar_personagem(nome:str):
    personagem=db.buscar("",nome)
    if personagem:
        return personagem
    raise HTTPException(status_code=404, detail="personagem não encontrado")
@app.post("/votar/{personagem}")
def upvote(personagem):
    voto=banco().atualizar_voto(personagem)
    if voto==0:
        return "adicionado com sucesso"
    elif voto==1:
        raise HTTPException(status_code=404, detail="personagem não encontrado")
    else:
        raise HTTPException(status_code=400, detail="problema no banco de dados")
