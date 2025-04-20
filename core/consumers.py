import asyncio

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncWebsocketConsumer


class TestConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the 'test_channel' group
        await self.channel_layer.group_add("test_channel", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        # Leave the group
        await self.channel_layer.group_discard("test_channel", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        # When we receive a message, broadcast it to the group
        # await self.channel_layer.group_send(
        #    "test_channel", {"type": "chat_message", "message": text_data}
        # )
        # Send a message to worker
        await self.channel_layer.send(
            "experiment", {"type": "do_work", "message": text_data}
        )

    async def chat_message(self, event):
        # Send the message to the WebSocket
        message = event["message"]
        await self.send(text_data=message)


class PrintConsumer(AsyncConsumer):
    async def do_work(self, message):
        print("Doing some work")
        await asyncio.sleep(5)
        print(message)
        await self.channel_layer.group_send(
            "test_channel", {"type": "chat_message", "message": "Work done"}
        )
