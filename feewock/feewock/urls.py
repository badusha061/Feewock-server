from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from user_auth.api import views

router = DefaultRouter()
router.register("user" , views.UserViewSet , basename="user")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/' , include('rest_framework.urls')),
    path('api/', include('user_auth.api.urls')), 
]
urlpatterns += router.urls
