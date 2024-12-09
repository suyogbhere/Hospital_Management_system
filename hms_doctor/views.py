from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from hms.models import *
from hms_doctor.models import *
from django.contrib.auth.decorators import login_required
from hms_doctor.forms import *


def Doctor_Profile(request):
    try:
        # Get the Patient object for the logged-in user
        doctor= Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        doctor = None
    return render(request, 'hms_doctor/doctor_profile.html',locals())
