from sqlalchemy import update
from sqlalchemy.orm import Session
from banco import User,engine

class consulta():
    def __init__(self):
        pass
    
    def buscar_no_elenco(self,ator=None,personagem=None,status=None,habilidade=None,mais_votado=False):
        with Session(engine) as session:
            if(ator==None and personagem ==None):
            # #
            # aqui faz a filtragem da pesquisa
            # #
                    if(status==None and habilidade==None and mais_votado==False):
                        busca=session.query(User.nome,User.ator,User.status,
                            User.habilidades,User.upvote).all()
                    else:
                        if(status!=None and habilidade!=None and mais_votado!= False):
                            busca=session.query(User.nome,User.ator,User.status,
                            User.habilidades,User.upvote).filter(User.status==status,User.habilidades==habilidade)
                        else:
                            busca=session.query(User.nome,User.ator,User.status,
                            User.habilidades,User.upvote)
                            if(status!=None):
                                busca=busca.filter(User.status==status)
                            if(habilidade!=None):
                                busca=busca.filter(User.habilidades==[habilidade])
                            if(mais_votado==True):
                        #ainda vou implementar calma manito
                                print
                    lista_de_dict=list()
                    dicionario=dict()
                    busca=busca.all()
                    try:
                        for c in range(0,len(busca)):
                            dicionario={"nome":busca[c][0],"ator":busca[c][1],"status":busca[c][2],
                            "habilidade":busca[c][3],"upvote":busca[c][4]}
                            lista_de_dict.append(dicionario)
                        return lista_de_dict
                    except IndexError:
                        for c in range(0,busca.count()):
                            dicionario={"nome":busca[c][0],"ator":busca[c][1],"status":busca[c][2],
                            "habilidade":busca[c][3],"upvote":busca[c][4]}
                            lista_de_dict.append(dicionario)
                        return lista_de_dict
            else:
        
                if(ator!=None):
                    dados=session.query(User.nome,User.ator,User.status,User.habilidades,User.upvote).filter(User.ator.ilike(f"{ator}%"))
                    return {"nome":dados[0][0],"ator":dados[0][1],"status":dados[0][2],"habilidade":dados[0][3],"upvote":dados[0][4]}
                else:
                    dados=session.query(User.nome,User.ator,User.status,User.habilidades,User.upvote).filter(User.nome.ilike(f"{personagem}%"))
                    return {"nome":dados[0][0],"ator":dados[0][1],"status":dados[0][2],"habilidade":dados[0][3],"upvote":dados[0][4]}
            
    def atualizar_voto(self,personagem):
         with Session(engine) as session:
            ##
            #esse User.ator.ilike ele nao faz diferenciaçao entre maiusculo ou minusculo 
            #  se tiver  john como parametro e aparecer jjjjohnnn ele vai pegar como se fosse 
            #john
            #  ##
            try:
                contagem=session.busca(User.upvote).filter(User.nome.ilike(f"{personagem}%"))
                atualizacao=update(User).filter(User.nome.ilike(f"{personagem}%")).values(upvote=contagem[0][0]+1)   
                session.execute(atualizacao)
                session.commit() 
                try:
                    contagem[0]
                except IndexError:
                    return 1
            except:
                return 2
            return 0
    
      
            


n1=consulta()
n1.buscar_no_elenco("vivo")