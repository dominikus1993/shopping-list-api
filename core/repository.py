from abc import ABC, abstractmethod
from typing import Awaitable, Coroutine
from core.model import CustomerID, CustomerShoppingList

class CustomerShoppingListWriter(ABC):
    @abstractmethod
    def store(self, customer_shopping_list: CustomerShoppingList) -> Coroutine:
        pass

    @abstractmethod
    def remove(self, customer_id: CustomerID) -> Coroutine:
        pass
    

class CustomerShoppingListReader(ABC):
    @abstractmethod
    def get(self, customer_id: CustomerID) -> Awaitable[CustomerShoppingList | None]:
        pass