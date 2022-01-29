import dataclasses
import json
from core.services import CustomerShoppingListChanged, CustomerShoppingListMessagePublisher, CustomerShoppingListRemoved
from dapr.clients import DaprClient

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)

class DaprCustomerShoppingListMessagePublisher(CustomerShoppingListMessagePublisher):

    async def publish(self, message: CustomerShoppingListChanged | CustomerShoppingListRemoved):
        with DaprClient() as client:
            client.publish_event("pubsub", "basket_events", json.dumps(message, cls=EnhancedJSONEncoder), data_content_type='application/json')
    