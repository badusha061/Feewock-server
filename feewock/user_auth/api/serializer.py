from rest_framework.serializers import ModelSerializer
from user_auth.models import Customer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


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


    
class CustomerTokenObtainPairSerialzer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        if user.is_superuser:
            data['is_admin'] = True
        elif hasattr(user , 'employee'):
            data['is_employee'] = True
        else:
            data['is_regular_user'] = True
            data['id'] = user.id
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['username'] = user.username
            data['email'] = user.email  
            data['number'] = user.number
            data['location'] = user.location
            data['is_active'] = user.is_active
        return data