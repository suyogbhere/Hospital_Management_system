from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    #  Define a model manager for user model with no username field
    def _create_user(self,email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email= self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password,  **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_patient', False)
        extra_fields.setdefault('is_doctor', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields._create_user( email, password, **extra_fields)  


    def create_superuser(self, email, password,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_patient', True)
        extra_fields.setdefault('is_doctor', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Staffuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_patient') is not True:
            raise ValueError('patient must have is_staff=True.')
        if extra_fields.get('is_doctor') is not True:
            raise ValueError('doctor must have is_staff=True.')

        return self._create_user( email, password, **extra_fields)