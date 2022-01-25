from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Awaitable, Coroutine, NewType

CustomerID = NewType("CustomerID", int)

@dataclass
class Item:
    item_quantity: int
    item_id: int
    
    def add_item_quantity(self, quantity: int) -> None:
        self.item_quantity += quantity
        

@dataclass
class CustomerShoppingList:
    customer_id: CustomerID
    items: list[Item]
    
    def add_item() -> None:
        print("add")

def empty_shopping_list(customer_id: CustomerID) -> CustomerShoppingList:
    return CustomerShoppingList(customer_id, [])

class CustomerShoppingListWriter(ABC):
    @abstractmethod
    def store(self, customer_shopping_list: CustomerShoppingList) -> Coroutine:
        pass
    

class CustomerShoppingListReader(ABC):
    @abstractmethod
    def get(self, customer_id: CustomerID) -> Awaitable[CustomerShoppingList | None]:
        pass