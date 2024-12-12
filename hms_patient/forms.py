from django import forms
from hms.models import *
from hms_patient.models import *
from datetime import datetime


class DateTimeInput(forms.DateTimeInput):
    input_type ='datetime-local'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
        # labels = 
        widgets={
            'Appointment_datetime': DateTimeInput(attrs={'class':'form-control'})
        }

    Appointment_ID = models.Aggregate(primary_key=True)
    Appointment_datetime = models.DateTimeField()
    Status = models.CharField(choices=Appointment_status, max_length=255,default='PENDING')
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    D_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)
