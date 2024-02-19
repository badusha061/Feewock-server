from rest_framework.generics import ListCreateAPIView
from .serializer import SerializerReviews , SerializerReviewsUserSide
from reviews.models import EmployeeReviews
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

@permission_classes([IsAuthenticated])
class Reviews(ListCreateAPIView):
    serializer_class = SerializerReviews
    queryset = EmployeeReviews.objects.all()



class ReviewsUserSide(APIView):
    serializer_class = SerializerReviewsUserSide
    def get(self , request , *args, **kwargs):
        employee_reviews =  EmployeeReviews.objects.filter(employee = self.kwargs['pk'])
        serializer = self.serializer_class(employee_reviews , many = True)
        return Response(data=serializer.data , status=status.HTTP_200_OK)
    

class AllReviewsList(APIView):
    serializer_class = SerializerReviewsUserSide
    def get(self ,request):
        queryset = EmployeeReviews.objects.all()[:8]
        serializer = self.serializer_class(queryset , many= True)
        return Response(data=serializer.data , status= status.HTTP_200_OK)