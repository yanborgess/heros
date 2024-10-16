from fastapi import FastAPI
from herois import *
from funcoes import *


app = FastAPI()

# OBTER TODOS OS HEROIS
@app.get('/herois')
def obter_herois():
    return herois

# OBTER HEROI POR ID
@app.get('/herois/{id}')
def obter_heroi_request(id: int):
    heroi_achado = obter_herois_id(id)
    return heroi_achado

#EDITAR HEROI
@app.put('/herois/{id}')
def editar_heroi_request(id: int, heroi_alterado: Heros):
    editar_heroi(id, heroi_alterado)

# CRIAR NOVO HEROI 
@app.post('/novoheroi')
def incluir_novo_request(novo_heroi: Heros):
    incluir_novo_heroi(novo_heroi)

# DELETAR HEROI
@app.delete('/heroidelet/{id}')
def excuir_heroi(id: int):
    deletar_heroi(id)

#EDITAR PODERES
@app.put('/editarpoderes')
def editar_poderes_request(id: int, novos_poder: str):
    editar_poderes(id, novos_poder)

#DELETAR TODOS OS HEROIS
@app.delete('/deletall')
def delet_all():
    herois.clear()
    return herois