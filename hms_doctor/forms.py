from django import forms
from hms.models import *
from hms_doctor.models import *
from django.utils.timezone import now



class DateTimeInput(forms.DateTimeInput):
    input_type ='datetime-local'

class AppointmentForm(forms.ModelForm):
    patient_name = forms.CharField(label="Patient Name", required=False,
                                   widget=forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}))
    class Meta:
        model = Appointment
        fields = ["Appointment_datetime","patient_name","Status"]
        # labels = {
        #     'P_ID':'Patient Name'
        # }
        widgets={
            'patient_name': forms.TextInput(attrs={'class':'form-control'}),
            'Appointment_datetime': DateTimeInput(attrs={'class':'form-control','readonly':'readonly'}),
            'Status': forms.Select(attrs={'class':'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            appointment = kwargs['instance']
            self.fields['patient_name'].initial = f"{appointment.P_ID.user.first_name} {appointment.P_ID.user.last_name}"
 

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['Medicine_name', 'Cost', 'Side_effect', 'P_ID']
        widgets = {
            'Medicine_name': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'cols': 10,
                'placeholder': 'Medicine Name......'
            }),
            'Cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'Side_effect': forms.Textarea(attrs={'class': 'form-control',
                'rows': 3,
                'cols': 10,
                'placeholder': 'Side effect......'}),
        }

    P_ID = forms.ModelChoiceField(
        queryset=Patient.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Patient"
    )




# class Prescribed(models.Model):
#     P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
#     Medicine_ID = models.ForeignKey(Medicine,on_delete=models.CASCADE)