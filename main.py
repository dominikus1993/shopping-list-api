from typing import Optional
import asyncio
from fastapi import FastAPI

from core.usecase import CustomerShoppingListDto

app = FastAPI()



@app.get("/{name}")
async def read_root(name: str):
    return {"Hello": name}


@app.get("/{customer_id}", response_model=CustomerShoppingListDto)
async def read_item(customer_id: int):
    result = [{"id": customer_id, "name": "John"}]
    return result



