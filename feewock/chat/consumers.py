import json 
from asgiref.sync import async_to_sync 
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Chat
from channels.db import database_sync_to_async

class TextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        sender_id, recipient_id = self.room_name.split('_')
 

        #creating room 
        self.room_group_name = f"chat_{sender_id}_{recipient_id}"


        #join the room
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):   
        #Leave the room
        await(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print('disocnnected',self.channel_layer)
        await super().disconnect(code)



    async def receive(self, text_data):
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        text = text_data_json['text']
        sender = text_data_json['sender']
        recipient_id = self.room_name.split('_')[1]
       
        chat_message = await self.save_chat_message(text , sender , recipient_id)

        if chat_message and not chat_message.is_read:
            chat_message.mark_as_read()
        messages = await self.get_messages(sender , recipient_id)
        # Send message to room group
        await(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': messages,
                'sender': sender
            }
        )

        await self.send(text_data=json.dumps({'message': 'Message received successfully!'}))
    
    async def chat_message(self, event):
        # Receive message from room group
        text = event['message']
        sender = event['sender']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'text': text,
            'sender': sender
        }))




    @database_sync_to_async
    def save_chat_message(self , message , sender_id , recipient_id):
        Chat.objects.create(message = message , sender_id = sender_id ,receiver_id = recipient_id)


    @database_sync_to_async
    def get_messages(self,sender ,recipient_id ):
        from .models import Chat
        from chat.api.serializer import ChatSerializer

        messages=[]
        for instance in Chat.objects.filter(sender__in =[sender , recipient_id] , receiver__in = [sender,recipient_id]):
            messages=ChatSerializer(instance).data

        return messages


class NoficationEmployee(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notification_%s' % self.room_name
        print(self.room_group_name)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def send_notification(self, event):
        message = json.loads(event['message'])
        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))



class NoficationUser(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'notification_%s' % self.room_name
        print(self.room_group_name)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def send_notificationuser(self, event):
        message = json.loads(event['message'])
        # Send message to WebSocket
        await self.send(text_data=json.dumps(message))