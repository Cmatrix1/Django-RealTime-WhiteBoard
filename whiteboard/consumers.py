import json
from channels.generic.websocket import AsyncWebsocketConsumer



class BoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("board_updates", self.channel_name)
        print("Accept The Connection !!!")
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
