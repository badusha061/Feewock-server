from .serializer import PostSerializer , LikesSerializer , PostSerializerUser
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import permission_classes
from post.models import Posts , Likes
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .pagination import PostListPagination
from rest_framework.pagination import PageNumberPagination

# @permission_classes([AllowAny])
class ListPosts(ListCreateAPIView):
    serializer_class = PostSerializerUser
    queryset = Posts.objects.all()
    pagination_class = PostListPagination



@permission_classes([AllowAny])
class ListPostIndivuallyUser(ListCreateAPIView):
    serializer_class = PostSerializerUser
    def get_queryset(self):
        employee_id = self.kwargs['pk']
        return Posts.objects.filter(employee = employee_id)


@permission_classes([IsAuthenticated])
class UpdatePost(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    lookup_field = 'pk'


@permission_classes([IsAuthenticated])
class ListPostIndivually(ListCreateAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        employee_id = self.kwargs['pk']
        print(employee_id)
        return Posts.objects.filter(employee = employee_id)
    


@permission_classes([IsAuthenticated])
class LikePost(ListCreateAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()



@permission_classes([IsAuthenticated])
class LikePostDelete(APIView):
    serializer_class = LikesSerializer
    def delete(self, request, pk, format=None):
        try:
            user = request.user 
            print('user is the ', user)
            Likes.objects.filter( user = user , post=pk).delete()
            return Response({"message": "Successfully deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    