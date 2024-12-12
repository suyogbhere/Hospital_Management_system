from django.contrib import admin
from hms.models import *
from hms_patient.models import *

# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display =['P_ID','get_user_first_name','get_user_last_name','get_user_email','get_user_mobile','Address']
    def save_model(self, request, obj, form, change):
        obj.save()  # Ensure the object is saved

    def get_user_first_name(self, obj):
        return obj.user.first_name
    get_user_first_name.short_description = 'First Name'

    def get_user_last_name(self, obj):
        return obj.user.last_name
    get_user_last_name.short_description = 'Last Name'

    def get_user_email(self, obj):
        return obj.user.email
    get_user_email.short_description = 'Email'

    def get_user_mobile(self, obj):
        return obj.user.mobile
    get_user_mobile.short_description = 'Mobile'
