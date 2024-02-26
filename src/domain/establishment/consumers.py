import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .establishment_models import Order


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.order_items = f'itens_{self.scope["url_route"]["kwargs"]["order_items"]}'
        await self.channel_layer.group_add(self.order_items, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.order_items, self.channel_name)
