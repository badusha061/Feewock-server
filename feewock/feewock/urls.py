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
    path('api/', include('user_auth.api.urls')), 
    path('dashboard/', include('dashboard.urls')),
    path('service/', include('service.urls')),
    path('offer/',include('offerservice.urls')),
    path('list/',include('listemployee.api.urls')),
    path('employees/', include('EmployeeProfile.api.urls')),
    path('chat/',include('chat.api.urls')),
    path('post/',include('post.api.urls')),
    path('banner/',include('banner.api.urls')),
    path('booking/', include('booking.api.urls')),
    path('payment/', include('payment.api.urls')),
    # path('reviews/', include('reviews.api.urls'))
]


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
