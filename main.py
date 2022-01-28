from typing import Optional
import asyncio
from fastapi import FastAPI

from core.usecase import CustomerShoppingListDto, GetCustomerShoppingListUseCase
from infrastructure.repository import DaprCustomerShoppingListReader

app = FastAPI()

get_customer_items = GetCustomerShoppingListUseCase(DaprCustomerShoppingListReader())

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/{customer_id}", response_model=CustomerShoppingListDto)
async def read_item(customer_id: int):
    result = await get_customer_items.execute(customer_id)
    return result



