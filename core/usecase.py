
from core.repository import CustomerID, CustomerShoppingList, CustomerShoppingListReader, CustomerShoppingListWriter, Item, empty_shopping_list
from dataclasses import dataclass

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
      
      

@dataclass
class ItemDto:
    item_id: int
    item_quantity: int
    
    @staticmethod
    def from_item(item: Item):
        return ItemDto(item.item_id, item.item_quantity)
    
@dataclass
class CustomerShoppingListDto:
    customer_id: int
    items: list[ItemDto]   
    
    @staticmethod
    def from_basket(customer_basket: CustomerShoppingList):
        return CustomerShoppingListDto(customer_basket.customer_id, [ItemDto.from_item(item) for item in customer_basket.items])
    
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

    def __init__(self, reader: CustomerShoppingListReader, writer: CustomerShoppingListWriter) -> None:
        self.__reader = reader
        self.__writer = writer

    async def execute(self, customer_id:int):
        customer_id = CustomerID(customer_id)
        basket = await self.__reader.get(customer_id)
        
        if basket is not None:
            await self.__writer.remove(customer_id=customer_id)
