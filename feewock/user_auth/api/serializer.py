from rest_framework.serializers import ModelSerializer
from user_auth.models import Customer

class UserSerialzer(ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','first_name','last_name','username','email','number','location','password','is_active']
        extra_kwargs = {
            'password':{'write_only':True},
        }
    def create(self,validated_data):
        user = Customer.objects.create_user(**validated_data)
        return user
