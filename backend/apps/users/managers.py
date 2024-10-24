from django.contrib.auth.models import BaseUserManager as Manager


class UserManager(Manager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have an email')
        if not password:
            raise ValueError('Users must have a password')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_premium', True)

        if extra_fields['is_staff'] is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields['is_superuser'] is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields['is_active'] is not True:
            raise ValueError('Superuser must have is_active=True')
        user = self.create_user(email, password, **extra_fields)
        return user

