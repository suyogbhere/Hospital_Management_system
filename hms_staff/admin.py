from django.contrib import admin
from hms.models import *
from hms_staff.models import *


# Register your models here.
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display =['Staff_ID','user__first_name','user__last_name','user__email','user__mobile','Role']
    def save_model(self, request, obj, form, change):
        obj.save()  # Ensure the object is saved