from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.id} - {self.username} - {self.email} - {self.role}"

class Packages(models.Model):
    package_id = models.CharField(max_length=10, primary_key=True)
    package_name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.package_id} - {self.package_name} - {self.description} - {self.price}"

class Activities(models.Model):
    id = models.AutoField(primary_key=True)
    activity_id = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.activity_id} - {self.name}"

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    service_id = models.CharField(max_length=10, unique=True)
    service_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.service_id} - {self.service_name}"