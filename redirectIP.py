#!/usr/bin/env python3s
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
import json

redirect = os.getenv("redirectIP")
address = "http://" + redirect + ":5000"
app = FastAPI()

class Tarefa(BaseModel):
    nome: str

@app.get("/healthcheck/")
async def hello():
    response = requests.get(url = address + "/healthcheck/")
    return response.json()

@app.get("/Tarefa/")
async def listar():
    response = requests.get(url = address + "/Tarefa/")
    return response.json()

@app.post("/Tarefa/")
async def add(tarefa: Tarefa):
    data = { "nome": tarefa.nome }
    response = requests.post(url = address + "/Tarefa/", data= json.dumps(data))
    return response.json()
