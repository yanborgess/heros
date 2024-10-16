from herois import *

# OBTER HEROI POR ID 
def obter_herois_id(id: int )-> Heros:
    for heroi in herois:
        if heroi.id == id:
            return heroi 

# EDITAR HEROI
def editar_heroi (id, heroi_alterado: Heros) -> dict:
    for indice, heroi in enumerate(herois):
        if heroi.id == id:
            herois[indice]= heroi_alterado
            return heroi
        
# INCLUIR NOVO HEROI
def incluir_novo_heroi(novo_heroi:Heros):
    novo_heroi.id = len(herois) + 1
    herois.append(novo_heroi)
    return novo_heroi

# DELETAR HEROI
def deletar_heroi(id):
    for indice, heroi in enumerate(herois):
        if heroi.id == id:
            herois.pop(indice)
            return {"message": "Heroi excluído com sucesso"}
    return {}

# EDITAR PODER DO HEROI 
def editar_poderes(id, novos_poder: str):
    for indice, heroi in enumerate(herois):
        if heroi.id == id:
            herois[indice].poderes = novos_poder
            return novos_poder