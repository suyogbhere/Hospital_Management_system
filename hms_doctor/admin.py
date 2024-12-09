from django.contrib import admin
from hms.models import *
from hms_doctor.models import *


# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display =['D_ID','user__first_name','user__last_name','user__email','user__mobile','Department']
    def save_model(self, request, obj, form, change):
        obj.save()  # Ensure the object is saved