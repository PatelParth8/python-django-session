from django.contrib import admin
from .models import  registerdata

# Register your models here.
class showregisterdata(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']

admin.site.register(registerdata,showregisterdata)