from dataclasses import dataclass

from core.model import CustomerShoppingList, Item


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