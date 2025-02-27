from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from hms.models import *


GENDER_CHOICE=[
    ('Male','Male'),
    ('Female','Female')
]


class Patient_Registration(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    
    class Meta:
        model= User
        fields= ['email','first_name','last_name','mobile','is_patient','gender']
        widgets={"first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),
                 "mobile":forms.NumberInput(attrs={"class":"form-control"}),
                 }
    field_order = ['email','first_name','last_name','mobile','password1','password2','gender','is_patient']
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if mobile and (len(str(mobile)) != 10):
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile


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
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if mobile and (len(str(mobile)) != 10):
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile

class Doctor_Registration(UserCreationForm):
    password1= forms.CharField(label='password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2= forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    
    class Meta:
        model= User
        fields= ['email','first_name','last_name','mobile','gender']
        widgets={"first_name":forms.TextInput(attrs={"class":"form-control"}),
                 "last_name":forms.TextInput(attrs={"class":"form-control"}),
                 "email":forms.EmailInput(attrs={"class":"form-control"}),
                 "mobile":forms.NumberInput(attrs={"class":"form-control"}),
                 }
    field_order = ['email','first_name','last_name','mobile','password1','password2','gender']
    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if mobile and (len(str(mobile)) != 10):
            raise forms.ValidationError("Mobile number must be exactly 10 digits.")
        return mobile

class PatientLogin(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","autofocus":True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","autofocus":True}))

class StaffLogin(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","autofocus":True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","autofocus":True}))

class DoctorLogin(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","autofocus":True}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","autofocus":True}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {'fname':'Full Name', 'contact':'Contact Number', 'email':'Email Id', 'subject':'Subject', 'message':'Message' }
        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control','placeholder':'Full Name'}),
            'contact':forms.NumberInput(attrs={'class':'form-control','placeholder':'Contact Number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email ID'}),
            'subject':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Subject'}),
            'message':forms.Textarea(attrs={    
                'class':'form-control',
                'rows':3,
                'cols':10,
                'placeholder':'Message......'
                })
        }
    def clean_contact(self):
        contact = self.cleaned_data.get('contact')

        if not contact.isdigit():
            raise forms.ValidationError("Contact number must contain only digits.")

        if len(contact) != 10:
            raise forms.ValidationError("Contact number must be exactly 10 digits.")

        return contact