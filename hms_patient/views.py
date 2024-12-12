from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from hms.models import *
from hms_patient.models import *
from django.contrib.auth.decorators import login_required
from hms_patient.forms import *

# Create your views here.
def Patient_Profile(request):
    try:
        # Get the Patient object for the logged-in user
        patient= Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = None
    return render(request, 'hms_patient/patient_profile.html',locals())


def Book_Appointment(request):
    try:
        # Appintment booking
        appointment= Appointment.objects.get(user=request.user)
    except Appointment.DoesNotExist:
        appointment = None
    return render(request, 'hms_patient/book_appointment.html',locals())