from chat.models import Chat
from rest_framework.serializers import ModelSerializer
from user_auth.api.serializer import UserSerializer

class ChatSerializer(ModelSerializer):
    sender = UserSerializer(read_only = True)
    receiver = UserSerializer(read_only = True)
    class Meta:
        model = Chat
        fields = ['id','sender','receiver','messge','date','is_read']