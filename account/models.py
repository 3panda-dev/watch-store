from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser, 
    PermissionsMixin
)

from datetime import datetime, timedelta
from random import randint

class UserManager(BaseUserManager):
    def create_user(self, phone , email, password=None, **extra_fields):
        #make sure phone number , password and email is valid
        if not email:
            raise ValueError('email needs to be set')
        if not phone:
            raise ValueError("please enter a phone number")
        if not password:
            raise ValueError("password needs to be set")

        normalized_email = self.normalize_email(email)
        
        user = self.model(phone=phone,
                        email=normalized_email,
                        **extra_fields,
                        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self.create_user(phone, password, **extra_fields)

    def user_verify(self):
        generated_code = self.model.generate_code
        code = generated_code.get('code')
        exp_date = generated_code.get('exp_date')

        if code == self.model.verify:
            pass












class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=11)
    is_verified = models.BooleanField(default=False)
    verify = models.CharField(max_length=6)
    exp_verify_code = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'phone'

    @property
    def generate_code(self):
        expiry_date = datetime.now() + timedelta(minutes=5)
        code = randint(111111, 999999)

        return{'code': code, 
               'exp_date': expiry_date,
               }





        
        
        

        


