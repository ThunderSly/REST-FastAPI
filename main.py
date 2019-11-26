#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import pymongo

dbIP = os.getenv("mongoIP")
dbAddress = "mongodb://" + dbIP + ":27017/"
clientMongo = pymongo.MongoClient(dbAddress)
database = clientMongo['RaulDB']
db = database['databaseMongo']

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
