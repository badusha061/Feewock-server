# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import  UserModel
from employee_auth.models import Employees

class EmployeesBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Employees.objects.get(email=email)
        except Employees.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Employees.objects.get(pk=user_id)
        except Employees.DoesNotExist:
            return None

class UserModelBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
