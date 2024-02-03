from django.urls import path
from .views import ListPosts , ListPostIndivually , UpdatePost  , ListPostIndivuallyUser

urlpatterns = [    
    #listing post in user side without permision 
    path('list', ListPosts.as_view() , name='listing-post'),

    #post listing and updating and delete in employee side
    path('list/<int:pk>/', ListPostIndivually.as_view() , name='listing-post'),
    path('listuser/<int:pk>/', ListPostIndivuallyUser.as_view() , name='listing-post'),
    path('update/<int:pk>/', UpdatePost.as_view() , name='deleting-post'),   
]
