from django.contrib import admin
from .models import Chat , EmployeeNotification , UserNotification
# Register your models here.
admin.site.register(Chat)
admin.site.register(EmployeeNotification)
admin.site.register(UserNotification)