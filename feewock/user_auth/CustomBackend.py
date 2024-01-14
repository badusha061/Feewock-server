from user_auth.models import UserModel
from employee_auth.models import Employees
from django.contrib.auth.backends import BaseBackend

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            print(f"Trying to authenticate user with email: {username}")
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                print("User authenticated successfully.")
                return user
        except UserModel.DoesNotExist:
            pass

        try:
            print(f"Trying to authenticate employee with email: {username}")
            employee = Employees.objects.get(email=username)
            if employee.check_password(password):
                print("Employee authenticated successfully.")
                return employee
        except Employees.DoesNotExist:
            pass

        print(f"Authentication failed for email: {username}")
        return None
