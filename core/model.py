from typing import NewType
from attr import dataclass
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
        index = find_index_by(self.items, lambda i: i.item_id == item.item_id)
        if index is None:
            self.items.append(item)
        else:
            self.items[index].add_item_quantity(item.item_quantity)

    def remove_item(self, item: Item) -> None:
        index = find_index_by(self.items, lambda i: i.item_id == item.item_id)
        if  index is not None:
            basket_item = self.items[index]
            basket_item.sub_item_quantity(item.item_quantity)
            if not basket_item.has_items():
                self.items.remove(basket_item)

def empty_shopping_list(customer_id: CustomerID) -> CustomerShoppingList:
    return CustomerShoppingList(customer_id, [])