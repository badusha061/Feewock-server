from django.db import models
from employee_auth.models import Employees
# Create your models here.

class EmployeesAvailability(models.Model):
    employees = models.ForeignKey(Employees, on_delete=models.CASCADE)
    date = models.DateField(unique = True)
    is_available  = models.BooleanField(default = True)

    def __str__(self) -> str:
        return self.employees.username


