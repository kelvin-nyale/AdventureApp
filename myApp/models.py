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

# class Bookings(models.Model):
#     user = models.ForeignKey(Users, on_delete=models.CASCADE)
#     activities = models.ManyToManyField(Activities, blank=True)
#     package = models.ForeignKey(Packages, on_delete=models.SET_NULL, null=True, blank=True)
#     pax = models.PositiveIntegerField()  # Number of people
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     booking_date = models.DateField()  # Captures the user's selected date of visit

#     def __str__(self):
#         return f"Booking {self.id} by {self.user.username} on {self.booking_date}"

class Rooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10, unique=True)
    room_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.room_id} - {self.room_number} - {self.room_name}"
  