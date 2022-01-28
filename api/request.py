
from pydantic import BaseModel

class AddItemToCustomerShoppingListRequest(BaseModel):
    item_quantity: int
    item_id: int