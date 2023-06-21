import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Participant, Message


class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("board_updates", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("board_updates", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "board_updates",
            {
                "type": "broadcast_message",
                "data": data,
                "sender_channel_name": self.channel_name,
            },
        )

    async def broadcast_message(self, event):
        if self.channel_name != event["sender_channel_name"]:
            await self.send(text_data=json.dumps(event["data"]))




class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.create_message(message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': self.user.username
            }
        )


    async def chat_message(self, event):
        if not self.user.name == event['username']:
            await self.send(text_data=json.dumps({
                'message': event['message'],
                'username': event['username']
            }))


    # Write method for validation of sender name

    @database_sync_to_async
    def create_message(self, message):
        # Could Be better
        participant = Participant.objects.get(user=self.user, room__slug=self.room_name)
        Message.objects.create(sender=participant, room=participant.room, content=message)