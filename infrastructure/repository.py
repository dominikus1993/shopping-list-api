import json
from dapr.clients import DaprClient
from dapr.clients.grpc._request import TransactionalStateOperation, TransactionOperationType
from dapr.clients.grpc._state import StateItem
from core.repository import CustomerID, CustomerShoppingList, CustomerShoppingListReader, CustomerShoppingListWriter, Item
import dataclasses, json

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

class DaprCustomerShoppingListReader(CustomerShoppingListReader):

    async def get(self, customer_id: CustomerID):
        with DaprClient() as client:
            result = client.get_state(
                'statestore',
                str(customer_id)
            )
            if result is None or result.data is None or result.data == b'':
                return None
            else:
                data = json.loads(result.data.decode('utf-8'))
                items = []
                for item in data["items"]:
                    print(item)
                    items.append(Item(item["item_id"], item["item_quantity"]))
                return CustomerShoppingList(customer_id, items)

class DaprCustomerShoppingListWriter(CustomerShoppingListWriter):

    async def store(self, customer_shopping_list: CustomerShoppingList):
        with DaprClient() as client:
            client.execute_state_transaction(store_name='statestore', operations=[
                TransactionalStateOperation(
                    operation_type=TransactionOperationType.upsert,
                    key=str(customer_shopping_list.customer_id),
                    data=json.dumps(customer_shopping_list, cls=EnhancedJSONEncoder))])

    async def remove(self, customer_id: CustomerID):
        with DaprClient() as client:
            client.delete_state(store_name='statestore', key=str(customer_id))

