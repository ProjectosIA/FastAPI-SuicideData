from fastapi import FastAPI
from main import data

api = FastAPI()

@api.get("/data")
async def GetData():
    
    return str(data)