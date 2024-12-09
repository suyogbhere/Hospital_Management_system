from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from hms.models import *
from django.contrib.auth.decorators import login_required
from hms.forms import *

# Create your views here.
def Staff_Profile(request):
    try:
        # Get the Patient object for the logged-in user
        staff= Staff.objects.get(user=request.user)
    except Staff.DoesNotExist:
        staff = None
    return render(request, 'hms/Staff_Profile.html')

