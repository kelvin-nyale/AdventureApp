from django.contrib import admin
from .models import Users, Packages, Activities

# Register your models here.
admin.site.register(Users)
admin.site.register(Packages)
admin.site.register(Activities)
