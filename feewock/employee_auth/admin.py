from django.contrib import admin
from .models import EmployeePostion , Employees , BankDetails 
# Register your models here.
admin.site.register(BankDetails)
admin.site.register(EmployeePostion)
admin.site.register(Employees)

