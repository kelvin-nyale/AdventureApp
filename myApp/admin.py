from django.contrib import admin
from .models import Users, Packages, Activities, Services

# Register your models here.
admin.site.register(Users)
admin.site.register(Packages)
admin.site.register(Activities)
admin.site.register(Services)
