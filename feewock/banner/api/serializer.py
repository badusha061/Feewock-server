from rest_framework.serializers import ModelSerializer
from banner.models import UserBanner

class UserBannerSerializer(ModelSerializer):
    class Meta:
        model = UserBanner
        fields = ['id','titile','image']
    