from re import I
from typing import Any
from fastapi import FastAPI
from dapr.ext.fastapi import DaprApp
import uvicorn
from api.request import AddItemToCustomerShoppingListRequest

from core.usecase import AddItemToCustomerShoppingListCommand, AddItemToCustomerShoppingListUseCase, CustomerShoppingListDto, GetCustomerShoppingListUseCase
from infrastructure.repository import DaprCustomerShoppingListReader, DaprCustomerShoppingListWriter

app = FastAPI()
dapr_app = DaprApp(app)
get_customer_items = GetCustomerShoppingListUseCase(DaprCustomerShoppingListReader())
add_item = AddItemToCustomerShoppingListUseCase(DaprCustomerShoppingListReader(), DaprCustomerShoppingListWriter())

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/basket/{customer_id}", response_model=CustomerShoppingListDto)
async def read_item(customer_id: int):
    result = await get_customer_items.execute(customer_id)
    return result

@app.post("/basket/{customer_id}", status_code=201)
async def create_item(customer_id: int, item: AddItemToCustomerShoppingListRequest):
    await add_item.execute(AddItemToCustomerShoppingListCommand(customer_id, item.item_id, item.item_quantity))
    return {"message": "ok"}

if __name__ == "__main__":
    application: Any = app 
    uvicorn.run(application, host="0.0.0.0", port=8000)