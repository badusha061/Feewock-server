from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from user_auth.api import views
from employee_auth.views import Employees

router = DefaultRouter()
router.register("user" , views.UserViewSet , basename="user")
router.register("employee",Employees , basename='employee' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/' , include('rest_framework.urls')),
    path('api/', include('user_auth.api.urls')), 
    path('dashboard/', include('dashboard.urls')),
    path('service/', include('service.urls')),
]
urlpatterns += router.urls
