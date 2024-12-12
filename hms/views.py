from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from hms.models import *
from django.contrib.auth.decorators import login_required
from hms.forms import *

# Create your views here.
def Home(request):
    return render(request, 'hms/home.html')

def About(request):
    return render(request, 'hms/about.html')

def Contact(request):
    return render(request, 'hms/contact.html')

def Register(request):
    return render(request, 'hms/register.html')


def User_Login(request):
    return render(request, 'hms/login.html')


def Patient_Register(request):
    if request.method == 'POST':
        fm = Patient_Registration(request.POST)
        try:
            if fm.is_valid():
                fm.save()
                messages.success(request,'Account Created successfully')
                return HttpResponseRedirect('/patient_login/')
        except:
            pass
    else:
        fm = Patient_Registration()
    return render(request, 'hms/patient_register.html',{'form':fm})

def Patient_Login(request):
    error = ''
    if request.method == 'POST':
        fm= PatientLogin(data=request.POST, request=request)
        try:
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                print('username:',username)
                print('password:',password)
                user = authenticate(username=username, password=password)
                if user.is_patient:
                    login(request,user)
                    messages.success(request,'Login successfully !!')
                    return HttpResponseRedirect('/hms_patient/Patient_Profile/')
                else:
                    messages.warning(request,'You are not yet patient, Kindly contact to admin !!')
        except:
            messages.danger(request,'Something went wrong!!, Try again')
    else:
        fm = PatientLogin()
    return render(request, 'hms/patient_login.html',locals())

def Logout(request):
    logout(request)
    messages.success(request,'Logout successfully !!')
    return redirect('login')


def Staff_Register(request):
    if request.method == 'POST':
        fm = Staff_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created successfully')
            return HttpResponseRedirect('/staff_login/')
    else:
        fm = Staff_Registration()
    return render(request, 'hms/staff_register.html',{'form':fm})

def Staff_Login(request):
    if request.method == 'POST':
        fm= StaffLogin(data=request.POST, request=request)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print('username:',username)
            print('password:',password)
            user = authenticate(username=username, password=password)
            if user.is_staff:
                login(request,user)
                messages.success(request,'Login successfully')
                return HttpResponseRedirect('/hms_staff/Staff_Profile/')
            else:
                    messages.warning(request,'You are not yet hospital staff, Kindly contact to admin!!')
    else:
        fm= StaffLogin()
    return render(request, 'hms/staff_login.html',{'form':fm})

def Doctor_Register(request):
    if request.method == 'POST':
        fm = Doctor_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created successfully')
            return HttpResponseRedirect('/doctor_login/')
    else:
        fm = Doctor_Registration()
    return render(request, 'hms/doctor_register.html',{'form':fm})

def Doctor_Login(request):
    if request.method == 'POST':
        fm= DoctorLogin(data=request.POST, request=request)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print('username:',username)
            print('password:',password)
            user = authenticate(username=username, password=password)
            if user.is_doctor:
                login(request,user)
                messages.success(request,'Login successfully')
                return HttpResponseRedirect('/hms_doctor/doctor_profile/')
            else:
                    messages.warning(request,'You are not yet doctor, Kindly contact to admin !!')
    else:
        fm= DoctorLogin()
    return render(request, 'hms/doctor_login.html',{'form':fm})


def Contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request,'Data submitted successfully !!!')
        except Exception as e:
            print(e)
            messages.danger(request,'Something went wrong !!!')
    else:
        form = ContactForm()
    return render(request, 'hms/contact.html',locals())