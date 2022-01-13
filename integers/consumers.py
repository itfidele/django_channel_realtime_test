import json
from random import randint
from channels.consumer import SyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncJsonWebsocketConsumer
from time import sleep
from .models import Data
from channels.db import database_sync_to_async
from asgiref.sync import async_to_sync,sync_to_async




class WSConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("well", self.channel_name)

        
    async def receive_json(self, message):
        print("receive",message)
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("hello", self.channel_name)

    async def data_update(self,event):
        await self.send_json(event)
