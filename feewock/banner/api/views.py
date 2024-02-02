from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from banner.models import UserBanner
from .serializer import UserBannerSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes


# @permission_classes([IsAdminUser])
class ListUserBanner(ListCreateAPIView):
    serializer_class = UserBannerSerializer
    queryset = UserBanner.objects.all()


# @permission_classes([IsAdminUser])
class UpdateUserBanner(RetrieveUpdateDestroyAPIView):
    serializer_class = UserBannerSerializer
    queryset = UserBanner.objects.all()