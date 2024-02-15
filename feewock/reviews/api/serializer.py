from rest_framework.serializers import ModelSerializer
from reviews.models import EmployeeReviews
from user_auth.api.serializer import UserIndvualSerializers

class SerializerReviews(ModelSerializer):
    class Meta:
        model = EmployeeReviews
        fields = ['id','user','employee','content','star_rating','created_at']



class SerializerReviewsUserSide(ModelSerializer):
    user = UserIndvualSerializers()
    class Meta:
        model = EmployeeReviews
        fields = ['id','user','employee','content','star_rating','created_at']
