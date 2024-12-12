from django.contrib import admin
from hms.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =['id','first_name','last_name','email','mobile','gender','is_active','is_staff','is_patient','is_doctor']

    