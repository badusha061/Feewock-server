from .serializer import PostSerializer , LikesSerializer , PostSerializerUser
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework.decorators import permission_classes
from post.models import Posts , Likes
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

@permission_classes([AllowAny])
class ListPosts(ListCreateAPIView):
    serializer_class = PostSerializerUser
    queryset = Posts.objects.all()


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



