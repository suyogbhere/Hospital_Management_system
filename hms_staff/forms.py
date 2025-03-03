from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from hms.models import *


GENDER_CHOICE=[
    ('Male','Male'),
    ('Female','Female')
]


class Staff_Registration(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    
    class Meta:
        model= User
        fields= ['email','first_name','last_name','mobile','gender']
        widgets={"first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),
                 "mobile":forms.NumberInput(attrs={"class":"form-control"}),
                 }
    field_order = ['email','first_name','last_name','mobile','password1','password2','gender']
   


class StaffLogin(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","autofocus":True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","autofocus":True}))



class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['P_ID', 'Total_amount', 'Pay_date', 'Pay_method']
        widgets = {
            'P_ID': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap dropdown
            'Total_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'Pay_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Pay_method': forms.Select(attrs={'class': 'form-select'}),  # Bootstrap dropdown
        }