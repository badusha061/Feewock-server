from django.urls import path
from .views import ListPosts , ListPostIndivually , UpdatePost

urlpatterns = [    
    path('list', ListPosts.as_view() , name='listing-post'),
    path('list/<int:pk>/', ListPostIndivually.as_view() , name='listing-post'),
    path('update/<int:pk>/', UpdatePost.as_view() , name='deleting-post'),   
]
