from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
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
        if fm.is_valid():
            fm.save()
            msg='Account created succussfully!!!'
            return HttpResponseRedirect('/patient_login/')
    else:
        fm = Patient_Registration()
    return render(request, 'hms/patient_register.html',{'form':fm})

def Patient_Login(request):
    if request.method == 'POST':
        fm= AuthenticationForm(data=request.POST, request=request)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print('username:',username)
            print('password:',password)
            user = authenticate(username=username, password=password)
            if request.user.is_patient:
                login(request,user)
                return HttpResponseRedirect('/patient_dashboard/')
    else:
        fm= AuthenticationForm()
    return render(request, 'hms/patient_login.html',{'form':fm})

def Patient_dashboard(request):
    return render(request, 'hms/patient_dashboard.html')


def Staff_Register(request):
    if request.method == 'POST':
        fm = Staff_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            msg='Account created succussfully!!!'
            return HttpResponseRedirect('/staff_login/')
    else:
        fm = Staff_Registration()
    return render(request, 'hms/staff_register.html',{'form':fm})

def Staff_Login(request):
    if request.method == 'POST':
        fm= AuthenticationForm(data=request.POST, request=request)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print('username:',username)
            print('password:',password)
            user = authenticate(username=username, password=password)
            if request.user.is_staff:
                login(request,user)
                return HttpResponseRedirect('/staff_dashboard/')
    else:
        fm= AuthenticationForm()
    return render(request, 'hms/staff_login.html',{'form':fm})

def Staff_dashboard(request):
    return render(request, 'hms/staff_dashboard.html')


def Doctor_Register(request):
    if request.method == 'POST':
        fm = Doctor_Registration(request.POST)
        if fm.is_valid():
            fm.save()
            msg='Account created succussfully!!!'
            return HttpResponseRedirect('/doctor_login/')
    else:
        fm = Doctor_Registration()
    return render(request, 'hms/doctor_register.html',{'form':fm})

def Doctor_Login(request):
    if request.method == 'POST':
        fm= AuthenticationForm(data=request.POST, request=request)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            print('username:',username)
            print('password:',password)
            user = authenticate(username=username, password=password)
            if request.user.is_doctor:
                login(request,user)
                return HttpResponseRedirect('/doctor_dashboard/')
    else:
        fm= AuthenticationForm()
    return render(request, 'hms/doctor_login.html',{'form':fm})

def Doctor_dashboard(request):
    return render(request, 'hms/doctor_dashboard.html')


# def register_user(request):
    # if not request.user.is_staff:  # Only admin or authorized staff can register users
    #     return redirect('register_user')

    # if request.method == 'POST':
    #     user_form = UserRegistrationForm(request.POST)
    #     if user_form.is_valid():
    #         user = user_form.save(commit=False)
    #         user.set_password(user_form.cleaned_data['password'])  # Hash the password
    #         user.save()

            # Handle role-specific data
            # if user.role == 'DOCTOR':
            #     doctor_form = DoctorForm(request.POST)
            #     if doctor_form.is_valid():
            #         doctor = doctor_form.save(commit=False)
            #         doctor.user = user
            #         doctor.save()
            # elif user.role == 'STAFF':
            #     staff_form = StaffForm(request.POST)
            #     if staff_form.is_valid():
            #         staff = staff_form.save(commit=False)
            #         staff.user = user
            #         staff.save()
            # elif user.role == 'PATIENT':
            #     patient_form = PatientForm(request.POST)
            #     if patient_form.is_valid():
            #         patient = patient_form.save(commit=False)
            #         patient.user = user
            #         patient.save()

            # return redirect('user_list')  # Redirect to a list of users or a success page
    # else:
    #     user_form = UserRegistrationForm()
    #     doctor_form = DoctorForm()
    #     staff_form = StaffForm()
    #     patient_form = PatientForm()

    # return render(request, 'hms/register_user.html', {
    #     'user_form': user_form,
    #     'doctor_form': doctor_form,
    #     'staff_form': staff_form,
    #     'patient_form': patient_form,
    # })


# def patient_registration(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.role = 'PATIENT'  # Enforce patient role
#             user.save()
#             return redirect('login')  # Redirect to login page
#     else:
#         form = UserRegistrationForm()

#     return render(request, 'patient_registration.html', {'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
            # Redirect based on role
    #         if user.role == 'DOCTOR':
    #             return redirect('doctor_dashboard')
    #         elif user.role == 'STAFF':
    #             return redirect('staff_dashboard')
    #         elif user.role == 'PATIENT':
    #             return redirect('patient_dashboard')
    #     else:
    #         return render(request, 'login.html', {'error': 'Invalid credentials'})
    # return render(request, 'login.html')


# @login_required
# def doctor_dashboard(request):
    # if request.user.role != 'DOCTOR':
        # return redirect('user_login')  # Restrict access
    # return render(request, 'doctor_dashboard.html')

# @login_required
# def staff_dashboard(request):
    # if request.user.role != 'STAFF':
    #     return redirect('user_login')
    # return render(request, 'staff_dashboard.html')

# @login_required
# def patient_dashboard(request):
    # if request.user.role != 'PATIENT':
    #     return redirect('user_login')
    # return render(request, 'patient_dashboard.html')