import json
from typing import Awaitable
from dapr.clients import DaprClient

from core.repository import CustomerID, CustomerShoppingList, CustomerShoppingListReader

class DaprCustomerShoppingListReader(CustomerShoppingListReader):

    async def get(self, customer_id: CustomerID):
        with DaprClient() as client:
            result = client.get_state(
                'statestore',
                str(customer_id)
            )           
            if result is None:
                return None
            else:
                return json.loads(result.data.decode('utf-8'))
            
            