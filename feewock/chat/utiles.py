from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from booking.models import EmployeeAction , Appointment
from chat.models import UserNotification , EmployeeNotification
from channels.db import database_sync_to_async

def notify_employee(employee_id , message):
    channel_layer = get_channel_layer()
    room_group_name = f"employee_{employee_id}"
    message_text = json.dumps(message)

    appointment_id = json.loads(message_text)['appointment_id']
    save_employee_notfication(appointment_id)

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

    action_id = json.loads(message_text)['action_id']

    save_user_notification(action_id)

    async_to_sync(channel_layer.group_send)(
    room_group_name,
        {
            'type': 'notificationuser',
            'message': message_text
        }
    )




def save_user_notification(action_id):
    instance = EmployeeAction.objects.get(id = action_id)
    UserNotification.objects.create(action = instance )



def save_employee_notfication(appointment_id):
    instance = Appointment.objects.get(id = appointment_id)
    EmployeeNotification.objects.create(appointment = instance)