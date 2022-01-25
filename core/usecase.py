
from core.repository import CustomerID, CustomerShoppingListReader, CustomerShoppingListWriter, Item, empty_shopping_list
from dataclasses import dataclass

@dataclass
class AddItemToCustomerShoppingListCommand:
    customer_id: int
    item_quantity: int
    item_id: int
    
class AddItemToCustomerShoppingListUseCase:
    __reader: CustomerShoppingListReader
    __writer: CustomerShoppingListWriter

    def __init__(self, reader: CustomerShoppingListReader, writer: CustomerShoppingListWriter) -> None:
        self.__reader = reader
        self.__writer = writer

    async def execute(self, item: AddItemToCustomerShoppingListCommand):
        customer_id = CustomerID(item.customer_id)
        basket = await self.__reader.get(customer_id)
        customer_basket = empty_shopping_list(customer_id) if basket is None else basket
        customer_basket.items.append(Item(item.item_quantity, item.item_id))
        await self.__writer.store(basket)
        