from django.contrib import admin
from hms.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display =['id','first_name','last_name','email','mobile','gender','is_active','is_staff','is_patient','is_doctor']

    
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display =['Appointment_ID','Appointment_datetime','Status']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['Depart_ID','Depart_Name']

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display=['Medicine_ID','P_ID','Medicine_name','Side_effect','Cost']


@admin.register(Prescribed)
class PrescribedAdmin(admin.ModelAdmin):
    list_display=['P_ID','Medicine_ID']

@admin.register(Assigned)
class AssignedAdmin(admin.ModelAdmin):
    list_display=['P_ID','P_ID']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['fname','contact','email','subject','message']

