from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Awaitable, Coroutine, NewType

from core.repository import CustomerID, Item
from core.usecase import ItemDto


@dataclass
class CustomerShoppingListChanged:
    customer_id: int
    item: ItemDto

class CustomerShoppingListMessagePublisher(ABC):
    
    @abstractmethod
    def publish(self, message: CustomerShoppingListChanged) -> Awaitable:
        pass
    