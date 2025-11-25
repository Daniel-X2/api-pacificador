from sqlalchemy import update, select
from sqlalchemy.orm import Session
from banco import engine,Elenco

class ElencoRepository():

    def __init__(self):
        pass
    
    def get_select(self):
        smt = select(Elenco)
        return smt

    def filtro_mais_votado(self,smt):  
        #smt = select(Elenco)
        smt = smt.order_by(Elenco.upvote.desc())
        return smt
    def filtro_status(self,status,smt):
        
        smt = smt.filter(Elenco.Vivo == status)
        return smt
    def filtro_habilidades(self,habilidade,smt):
        #smt = select(Elenco)
        smt = smt.filter(Elenco.habilidades.contains(habilidade))
        return smt
    def executar_all(self,smt):
        with Session(engine) as session:
            return session.scalars(smt).all()
    def executar_first(self,smt):
        with Session(engine) as session:
            return session.scalars(smt).first()   
    def update_voto(self,personagem):
        smt = (update(Elenco).filter(Elenco.nome.ilike(f"{personagem}%")).values(upvote=Elenco.upvote + 1))
        return smt
    def buscar_ator(self,nome,smt):
        smt = smt.filter(Elenco.ator.ilike(f"{nome}%"))
        return smt
    def buscar_personagem(self,nome,smt):
        smt = smt.filter(Elenco.nome.ilike(f"{nome}%"))
        return smt
