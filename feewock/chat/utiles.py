from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

def notify_employee(room_name , message):
    channel_layer = get_channel_layer()
    room_group_name = f"notification_{room_name}"
    message_text = json.dumps(message)
    async_to_sync(channel_layer.group_send)(
        room_group_name,
        {
            'type':'send_notification',
            'message': message_text
        }
    )
    


def notify_user(room_name , message):
    channel_layer = get_channel_layer()
    room_group_name = f"notification_{room_name}"
    message_text = json.dumps(message)
    async_to_sync(channel_layer.group_send)(
    room_group_name,
        {
            'type': 'notificationuser',
            'message': message_text
        }
    )
