from typing import Optional
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/{name}")
async def read_root(name: str):
    return {"Hello": name}


@app.get("/{customer_id}")
async def read_item(customer_id: int):
    result = [{"id": customer_id, "name": "John"}]
    return result



