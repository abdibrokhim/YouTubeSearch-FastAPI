from typing import Union
from fastapi import FastAPI
import app.config as config

app = FastAPI()

@app.get("/youtube_search")
async def query(api_key: str, query: str):
    return config.send_query(api_key, query)
