from .serializer import PostSerializer , LikesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from post.models import Posts , Likes
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

# @permission_classes([IsAuthenticated])
class ListPosts(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()


# @permission_classes([IsAuthenticated])
class UpdatePost(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    lookup_field = 'pk'


# @permission_classes([IsAuthenticated])
class ListPostIndivually(ListCreateAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        employee_id = self.kwargs['id']
        return Posts.objects.get(employee_id = employee_id)
    