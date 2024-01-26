import json 
from asgiref.sync import async_to_sync 
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Chat

class TextConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print('connecting is working')
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print('rooooooom')
        self.room_group_name = 'chat_%s' % self.room_name
        print('grooooooooooooooop')
        #join the room
        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        print('aceppppppppppppppppppppppppt')
        self.accept()

    async def disconnect(self, code):   
        print('disconnecting is working')
        #Leave the room
        await(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print('the recieve is working')
        # Receive message from WebSocket
        text_data_json = json.loads(text_data)
        text = text_data_json['text']
        sender = text_data_json['sender']
        Chat.objects.create(message = text , sender = sender ,receiver = self.scope['user'])
        # Send message to room group
        await(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text,
                'sender': sender
            }
        )

    async def chat_message(self, event):
        print('the chat message is working')
        # Receive message from room group
        text = event['message']
        sender = event['sender']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'text': text,
            'sender': sender
        }))



