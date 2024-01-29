from chat.models import Chat
from rest_framework.serializers import ModelSerializer
from user_auth.models import UserModel

class UserChatSeralizer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','email']

        
class ChatSerializer(ModelSerializer):
    sender = UserChatSeralizer(read_only = True)
    receiver = UserChatSeralizer(read_only = True)
    class Meta:
        model = Chat
        fields = ['id','sender','receiver','message','date','is_read']


        
class EmployeeChatSerializer(ModelSerializer):
    sender = UserChatSeralizer(read_only = True)
    receiver = UserChatSeralizer(read_only = True)
    class Meta:
        model = Chat
        fields = ['id','sender','receiver']