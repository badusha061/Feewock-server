from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin ,BaseUserManager , Permission

class UserManager(BaseUserManager):
    def create_user(self , email , password = None):
        if not email:
            raise ValueError("User must have a email")
        user = self.model(email = email)
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self, email , password):
        user = self.create_user(
            email=email , password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)
        return user
