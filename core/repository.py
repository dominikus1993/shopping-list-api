from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Awaitable, Coroutine, NewType

from core.utils import find_index_by

CustomerID = NewType("CustomerID", int)

@dataclass
class Item:
    item_id: int
    item_quantity: int
    
    def add_item_quantity(self, quantity: int) -> None:
        self.item_quantity += quantity
        
    def sub_item_quantity(self, quantity: int) -> None:
        self.item_quantity -= quantity 
    
    def has_items(self) -> bool:
        return self.item_quantity > 0       
        

@dataclass
class CustomerShoppingList:
    customer_id: CustomerID
    items: list[Item]
    
    def add_item(self, item: Item) -> None:
        index = find_index_by(self.items, lambda item: item.item_id == item.item_id)
        if  index == -1:
            self.items.append(item)
        else:
            self.items[index].add_item_quantity(item.item_quantity)

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