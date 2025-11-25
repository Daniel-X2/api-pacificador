
from pydantic_core import _pydantic_core
from repository.repo import ElencoRepository
from dto.dto import ElencoDto,serializar_lista
from erros import *
repository=ElencoRepository()
class ElencoService():

    def __init__(self):
        pass
    def buscar_com_filtro(self,vivo:bool=True,habilidade_:str=None,mais_votado_:bool=False):
        
        smt=repository.get_select()
        smt=repository.filtro_status(status=vivo,smt=smt)
        if(habilidade_!=None and habilidade_!="" ):
            if( len(habilidade_.strip())>3):
                smt=repository.filtro_habilidades(habilidade=habilidade_,smt=smt)
            else:
                raise ErroValorMinimo("habilidades",3,3)
        if (mais_votado_==True):
            smt=repository.filtro_mais_votado(smt=smt)#depois preciso sicronizar com os outros filtros
            dados=repository.executar_first(smt)
            try:
                return ElencoDto(Nome=dados.nome,
                      ator=dados.ator,
                      Vivo=dados.Vivo,
                      habilidades=dados.habilidades,
                      upvote=dados.upvote).model_dump()
            except  _pydantic_core.ValidationError:
                raise ErroValidacao
            except AttributeError:
                raise ErroNenhumResultado("filtros")
        dados=repository.executar_all(smt)
        
        if(len(dados)==0):
             raise ErroNenhumResultado("lista vazia")
        dados=serializar_lista(dados_=dados)
        return dados
    def buscar_ator(self,nome):
        if(len(nome)<3):
            raise ErroValorMinimo("nome",4,3)
        smt=repository.get_select()
        smt=repository.buscar_ator(nome,smt)
        dados=repository.executar_first(smt)
        try:
            return ElencoDto(Nome=dados.nome,
                      ator=dados.ator,
                      status=dados.status,
                      habilidades=dados.habilidades,
                      upvote=dados.upvote).model_dump()  
        except AttributeError:
            raise ErroNenhumResultado("nome")
        except _pydantic_core.ValidationError:
            raise ErroValidacao
    def buscar_personagem(self,nome):
        if(len(nome)<3):
            raise ErroValorMinimo("nome",4,3)
        smt=repository.get_select()
        smt=repository.buscar_personagem(nome,smt)
        dados=repository.executar_first(smt)
        try:    
            return ElencoDto(Nome=dados.nome,
                      ator=dados.ator,
                      status=dados.status,
                      habilidades=dados.habilidades,
                      upvote=dados.upvote).model_dump()
        except _pydantic_core.ValidationError:
            raise ErroValidacao
        except AttributeError:
            raise ErroNenhumResultado("Nome")
    def retornar_elenco(self):
        smt=repository.get_select()
        dados=repository.executar_all(smt)
        dados=serializar_lista(dados)
        return dados
