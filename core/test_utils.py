from re import sub
import unittest

from core.model import CustomerID, CustomerShoppingList, Item
from core.utils import find_index_by

class TestUtils(unittest.TestCase):
    def test_find_index_by_when_element_exists(self):
        items = [Item(1, 1), Item(2, 2), Item(3, 3)]
        subject = find_index_by(items, lambda item: item.item_id == 2)
        self.assertIsNotNone(subject)
        self.assertEqual(subject, 1)

    def test_find_index_by_when_element__not_exists(self):
        items = [Item(1, 1), Item(2, 2), Item(3, 3)]
        subject = find_index_by(items, lambda item: item.item_id == 5)
        self.assertIsNone(subject)