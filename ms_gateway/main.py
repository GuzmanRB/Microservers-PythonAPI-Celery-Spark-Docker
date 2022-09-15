from fastapi import FastAPI
from fastapi import Request, responses
from dotenv import load_dotenv
import os
import requests

load_dotenv(".env")
URL_NER=os.getenv("URL_NER")

app=FastAPI()

@app.post('/ner')
async def getNer(request:Request):
    data=await request.json()
    res=requests.post(URL_NER,json=data)
    return responses.JSONResponse({"RESPONSE":res.text})
