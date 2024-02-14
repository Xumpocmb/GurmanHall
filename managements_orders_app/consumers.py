import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.utils import timezone

from orders_app.models import Order


class OrderConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = "orders"
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def order_update(self, event):
        self.send(text_data=json.dumps({
            'event_type': 'order_update',
            'order_id': event['order_id'],
            'order_status_text': event['order_status_text'],
            'created_at': event['created_at'],
            'total_sum': event['total_sum'],
        }))

    def order_create(self, event):
        # order_create {'type': 'order_create', 'order_id': 25}
        order = Order.objects.get(id=event['order_id'])

        self.send(text_data=json.dumps({
            'event_type': 'order_create',
            'order_id': event['order_id'],
            'order_status_text': order.get_status_display(),
            'created_at': timezone.localtime(order.created_at).isoformat(),
            'total_sum': order.basket_history['total_sum'],
        }))


