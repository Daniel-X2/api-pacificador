from pydantic import BaseModel,Field
class ElencoDto(BaseModel):
    Nome:str =Field(min_length=3)
    ator:str = Field(min_length=3)
    Vivo:bool
    habilidades:list
    upvote:int

def serializar_lista( dados_):
        lista = list()
        
        for c in range(0, len(dados_)):
            lista.append(
                ElencoDto(
                    Nome=dados_[c].nome,
                    ator=dados_[c].ator,
                    Vivo=dados_[c].Vivo,
                    habilidades=dados_[c].habilidades,
                    upvote=dados_[c].upvote
                ).model_dump()
                )
        return lista