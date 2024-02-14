import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
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

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        order_id = text_data_json['order_id']
        print('Received data:', order_id)
        # Отправка данных в группу
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {'type': 'order_update', 'order_id': order_id}
        )
        print('Sent data to group:', self.room_group_name)

    # Обработка данных от группы
    def order_update(self, event):
        # Отправка данных обновления клиенту
        self.send(text_data=json.dumps({
            'order_id': event['order_id'],
            'order_status': event['order_status'],
            'order_status_text': event['order_status_text'],
            'created_at': event['created_at'],
            'total_sum': event['total_sum'],
        }))


