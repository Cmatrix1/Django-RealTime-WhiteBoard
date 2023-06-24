import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from message.models import Message
from conference.models import Participant, ConferenceRoom


class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f'board_{self.room_name}'
        self.room_object = await self.get_conference_room()
        
        self.user = self.scope['user']
        self.is_admin = await self.check_is_admin()
        self.is_participant = await self.check_is_participant()
        if self.is_admin or self.is_participant:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        if self.is_admin:
            await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "broadcast_message",
                "data": data,
                "sender_channel_name": self.channel_name,
            },
        )
        else:
            await self.disconnect()


    async def broadcast_message(self, event):
        if self.channel_name != event["sender_channel_name"]:
            await self.send(text_data=json.dumps(event["data"]))
    
    @database_sync_to_async
    def get_conference_room(self):
        return ConferenceRoom.objects.filter(slug=self.room_name).first()
    
    @database_sync_to_async
    def check_is_admin(self):
        return self.user.is_authenticated and self.room_object.is_admin(self.user)
    
    @database_sync_to_async
    def check_is_participant(self):
        return self.room_object.is_participant(self.user)