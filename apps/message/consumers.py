import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from message.models import Message
from conference.models import Participant


class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['slug']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']
        self.participant = await self.get_participant()
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.delete_participant()
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
                'username': self.participant.name
            }
        )


    async def chat_message(self, event):
        if not self.participant.name == event['username']:
            await self.send(text_data=json.dumps({
                'message': event['message'],
                'username': event['username']
            }))

    @database_sync_to_async
    def create_message(self, message):
        Message.objects.create(sender=self.participant, room=self.participant.room, content=message)

    @database_sync_to_async
    def get_participant(self):
        participant_id = self.scope['session'].get("participant_id")
        return Participant.objects.get(id=participant_id)

    @database_sync_to_async
    def delete_participant(self):
        return self.participant.delete()
