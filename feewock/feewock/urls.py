from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from user_auth.api import views
from employee_auth.views import Employees
from django.conf import settings 
from django.conf.urls.static import static

router = DefaultRouter()
router.register("user" , views.UserViewSet , basename="user")
router.register("employee",Employees , basename='employee' )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/' , include('rest_framework.urls')),
    path('api/api/', include('user_auth.api.urls')), 
    path('api/dashboard/', include('dashboard.urls')),
    path('api/service/', include('service.urls')),
    path('api/offer/',include('offerservice.urls')),
    path('api/list/',include('listemployee.api.urls')),
    path('api/employees/', include('EmployeeProfile.api.urls')),
    path('api/chat/',include('chat.api.urls')),
    path('api/post/',include('post.api.urls')),
    path('api/banner/',include('banner.api.urls')),
    path('api/booking/', include('booking.api.urls')),
    path('api/payment/', include('payment.api.urls')),
    path('api/reviews/', include('reviews.api.urls')),
    path('api/contact/', include('contact.api.urls')),
    path('api/admindashboard/', include('admindashboard.api.urls')),   
]


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
