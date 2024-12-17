from django import forms
from hms.models import *
from hms_patient.models import *
# from datetime import datetime
from django.utils.timezone import now


class DateTimeInput(forms.DateTimeInput):
    input_type ='datetime-local'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["Appointment_datetime","D_ID"]
        labels = {
            'D_ID':'Doctor Name'
        }
        widgets={
            # 'P_ID': forms.TextInput(attrs={'class':'form-control'}),
            'Appointment_datetime': DateTimeInput(attrs={'class':'form-control'}),
            'D_ID': forms.Select(attrs={'class':'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['D_ID'].queryset = Doctor.objects.all()
        self.fields['D_ID'].label_from_instance = lambda obj: f"{obj.user.first_name}{' '}{obj.user.last_name}"
         
    def clean_Appointment_datetime(self):
        datetime = self.cleaned_data['Appointment_datetime']
        if datetime < now():
            raise ValidationError("Appointment date and time must be in the future.")
        return datetime    

