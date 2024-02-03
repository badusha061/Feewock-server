from django.urls import path
from .views import ListUserBanner , UpdateUserBanner , ListUserBannerUser

urlpatterns = [  
    #User Banner in admin side
    path('list', ListUserBanner.as_view(), name='list-banner'),
    path('update/<int:pk>/', UpdateUserBanner.as_view(), name='update-banner'),


    #Employee Banner in admin side

    #User Banner in listing user side
    path('listuser', ListUserBannerUser.as_view(), name='list-banner'),
]