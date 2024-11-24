from django import forms
from django.contrib.auth.forms import UserCreationForm
from hms.models import *


class Patient_Registration(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput())
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields= ['email','first_name','last_name','mobile','is_patient','gender']
    field_order = ['email','first_name','last_name','mobile','password1','password2','gender','is_patient']



GENDER_CHOICE=[
    ('Male','Male'),
    ('Female','Female')
]

class Staff_Registration(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    class Meta:
        model= User
        fields= ['email','first_name','last_name','mobile','gender']
        widgets={"first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),
                 "mobile":forms.NumberInput(attrs={"class":"form-control"}),
                 "gender":forms.TextInput(attrs={"class":"form-RadioSelect"}),
                 }
    field_order = ['email','first_name','last_name','mobile','password1','password2','gender']
   

class Doctor_Registration(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput())
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput())
    
    class Meta:
        model= User
        fields= ['email','first_name','last_name','mobile','gender']
    field_order = ['email','first_name','last_name','mobile','password1','password2','gender']