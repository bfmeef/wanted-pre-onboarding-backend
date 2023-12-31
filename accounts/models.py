from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일은 반드시 입력되어야 합니다.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        if password:
            if len(password) < 8:
                raise ValidationError("비밀번호는 최소 8자 이상이어야 합니다.")

        user.set_password(password)
        user.save(using=self.db)
        return user

class CustomUser(AbstractBaseUser, PermissionError):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
