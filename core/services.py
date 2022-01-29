from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Awaitable
from core.dto import ItemDto


@dataclass
class CustomerShoppingListChanged:
    customer_id: int
    item: ItemDto
    event_type: str

@dataclass
class CustomerShoppingListRemoved:
    customer_id: int

class CustomerShoppingListMessagePublisher(ABC):
    
    @abstractmethod
    def publish(self, message: CustomerShoppingListChanged | CustomerShoppingListRemoved) -> Awaitable:
        pass
    