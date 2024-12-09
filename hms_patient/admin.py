from django.contrib import admin
from hms.models import *
from hms_patient.models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display =['P_ID','user__first_name','user__last_name','user__email','user__mobile','Address']
    def save_model(self, request, obj, form, change):
        obj.save()  # Ensure the object is saved
# admin.site.register(Patient)
