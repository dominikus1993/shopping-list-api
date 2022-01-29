
from pydantic import BaseModel

class AddItemToCustomerShoppingListRequest(BaseModel):
    item_quantity: int

class RemoveItemFromCustomerShoppingListRequest(BaseModel):
    item_quantity: int