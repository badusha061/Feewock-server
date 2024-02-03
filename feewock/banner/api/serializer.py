from rest_framework.serializers import ModelSerializer
from banner.models import UserBanner , EmployeeBanner

class UserBannerSerializer(ModelSerializer):
    class Meta:
        model = UserBanner
        fields = ['id','titile','image']
        read_only_fields = ["id"]



class EmployeeBannerSerializer(ModelSerializer):
    class Meta:
        model = EmployeeBanner
        fields = ['id','titile','image']
        read_only_fields = ["id"]
    