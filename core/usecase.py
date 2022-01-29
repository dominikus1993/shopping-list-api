from core.dto import CustomerShoppingListDto
from core.model import CustomerID, Item, empty_shopping_list
from core.repository import CustomerShoppingListReader, CustomerShoppingListWriter
from dataclasses import dataclass
from core.services import CustomerShoppingListChanged, CustomerShoppingListMessagePublisher, CustomerShoppingListRemoved

@dataclass
class AddItemToCustomerShoppingListCommand:
    customer_id: int
    item_id: int
    item_quantity: int
    
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
        customer_basket.add_item(Item(item.item_id, item.item_quantity))
        await self.__writer.store(customer_basket)
        

@dataclass
class RemoveItemFromCustomerShoppingListCommand:
    customer_id: int
    item_id: int
    item_quantity: int
    
class RemoveItemFromCustomerShoppingListUseCase:
    __reader: CustomerShoppingListReader
    __writer: CustomerShoppingListWriter

    def __init__(self, reader: CustomerShoppingListReader, writer: CustomerShoppingListWriter) -> None:
        self.__reader = reader
        self.__writer = writer

    async def execute(self, item: RemoveItemFromCustomerShoppingListCommand):
        customer_id = CustomerID(item.customer_id)
        basket = await self.__reader.get(customer_id)
        if basket is not None:
            basket.remove_item(Item(item.item_id, item.item_quantity))
            await self.__writer.store(basket)
      
    
class GetCustomerShoppingListUseCase:
    __reader: CustomerShoppingListReader

    def __init__(self, reader: CustomerShoppingListReader) -> None:
        self.__reader = reader

    async def execute(self, customer_id:int):
        customer_id = CustomerID(customer_id)
        basket = await self.__reader.get(customer_id)
        
        result = empty_shopping_list(customer_id) if basket is None else basket
        
        return CustomerShoppingListDto.from_basket(result)

class RemoveCustomerShoppingListUseCase:
    __reader: CustomerShoppingListReader
    __writer: CustomerShoppingListWriter
    __publisher: CustomerShoppingListMessagePublisher

    def __init__(self, reader: CustomerShoppingListReader, writer: CustomerShoppingListWriter, publisher: CustomerShoppingListMessagePublisher) -> None:
        self.__reader = reader
        self.__writer = writer
        self.__publisher = publisher

    async def execute(self, customer_id:int):
        customer_id = CustomerID(customer_id)
        basket = await self.__reader.get(customer_id)
        
        if basket is not None:
            await self.__writer.remove(customer_id=customer_id)
            await self.__publisher.publish(CustomerShoppingListRemoved(customer_id))
