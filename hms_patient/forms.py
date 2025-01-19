from django import forms
from hms.models import *
from hms_patient.models import *
# from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth import get_user_model


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

# User = get_user_model()

class PatientUpdateForm(forms.ModelForm):
    #Field from from patient model
    Address = forms.CharField(required=False, max_length=255,widget=forms.Textarea(attrs={
        'class':'form-control', 'rows':'2',
    }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'mobile']  # Fields from User model
        widgets={"first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control",'readonly': 'readonly'}),
                 "mobile":forms.NumberInput(attrs={"class":"form-control"}),
                 }
        
    def __init__(self, *args, **kwargs):
        patient = kwargs.pop('patient', None)  # Accept the Patient instance
        super().__init__(*args, **kwargs)

        # Pre-fill Patient-specific fields
        if patient:
            self.fields['Address'].initial = patient.Address

    def save(self, user_instance, patient_instance, commit=True):
        # Save the User model fields
        user_instance.first_name = self.cleaned_data['first_name']
        user_instance.last_name = self.cleaned_data['last_name']
        user_instance.mobile = self.cleaned_data['mobile']
        user_instance.email = self.cleaned_data['email']
        if commit:
            user_instance.save()
        # Save the Patient model fields
        patient_instance.Address = self.cleaned_data['Address']
        if commit:
            patient_instance.save()
        return user_instance