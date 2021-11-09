from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from MediaScanner import settings
from jsonfield import JSONField
import json

class DeveloperManager(BaseUserManager):
    def create_user(self, name, email, password, organisation):
        if not email:
            raise ValueError("Please provide us your email")
        email = self.normalize_email(email)
        developer = self.model(email = email, name = name, organisation = organisation)
        developer.set_password(password)
        developer.save(using = self._db)
        return developer
    
    def create_superuser(self, name, email, password, organisation):
        creator = self.create_user(name, email, password, organisation)
        creator.is_superuser = True
        creator.is_staff = True
        creator.save(using = self._db)
        return creator

class DeveloperProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique = True, max_length = 255, default = "scanner@email.com")
    name = models.CharField(max_length = 20, default = "Media Scanner")
    organisation = models.CharField(max_length = 20, default = "Media Scanner")
    is_staff = models.BooleanField(default = False)

    objects = DeveloperManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'organisation']

    def __str__(self):
        return self.email

class TextReportModel(models.Model):
    objects = DeveloperManager()
    developer_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )
    timing = models.DateTimeField(auto_now_add = True)
    parsed_text = models.TextField(max_length = 5000, default = "Write your text here")
    report = JSONField({})
    def __str__(self):
        return self.timing

