#!/usr/bin/env python3s
from fastapi import FastAPI
from pydantic import BaseModel
import os
import pymongo

dbIP = os.getenv("mongoIP")
dbAddress = "http://" + dbIP + ":27017"
clientMongo = pymongo.MongoClient(dbAddress)
db = clientMongo['databaseMongo']

app = FastAPI()

class Tarefa(BaseModel):
    nome: str

@app.post("/Tarefa/")
async def add(tarefa: Tarefa):
    tarefa = {"nome" : tarefa.nome}
    db.insert(tarefa)
    return

@app.get("/Tarefa/")
async def listar():
    tarefasDict = {}
    tarefasDict['Values'] = []
    for i in db.find():
        tarefasDict['Values'].append({'nome': i["nome"]})
    return tarefasDict


@app.get("/healthcheck/")
async def check():
    return 
