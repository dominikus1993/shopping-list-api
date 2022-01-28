from re import sub
import unittest

from core.repository import CustomerID, CustomerShoppingList, Item

class TestCustomerShoppingList(unittest.TestCase):
    def test_add_item_when_basket_is_empty(self):
        item = Item(1, 1)
        subject = CustomerShoppingList(CustomerID(1), [])
        subject.add_item(item)
        self.assertEqual(len(subject.items), 1)
        self.assertEqual(subject.items[0], Item(1, 1))

    def test_add_item_when_exists(self):
        item = Item(1, 1)
        subject = CustomerShoppingList(CustomerID(1), [Item(1, 2)])
        subject.add_item(item)
        self.assertEqual(len(subject.items), 1)
        self.assertEqual(subject.items[0], Item(1, 3))

    def test_add_new_item_when_exists(self):
        item = Item(2, 1)
        subject = CustomerShoppingList(CustomerID(1), [Item(1, 2)])
        subject.add_item(item)
        self.assertEqual(len(subject.items), 2)
        self.assertEqual(subject.items[0], Item(1, 2))
        self.assertEqual(subject.items[1], Item(2, 1))

    def test_remove_item_when_basket_is_empty(self):
        item = Item(1, 1)
        subject = CustomerShoppingList(CustomerID(1), [])
        subject.remove_item(item)
        self.assertEqual(len(subject.items), 0)

    def test_remove_item_when_exists(self):
        item = Item(1, 1)
        subject = CustomerShoppingList(CustomerID(1), [Item(1, 2)])
        subject.remove_item(item)
        self.assertEqual(len(subject.items), 1)
        self.assertEqual(subject.items[0], Item(1, 1))

    def test_remove_item_when_exists_and_quantity(self):
        item = Item(1, 1)
        subject = CustomerShoppingList(CustomerID(1), [Item(1, 1)])
        subject.remove_item(item)
        self.assertEqual(len(subject.items), 0)