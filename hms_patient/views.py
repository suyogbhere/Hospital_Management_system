from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from hms.models import *
from hms_patient.models import *
from django.contrib.auth.decorators import login_required
from hms_patient.forms import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden


# Create your views here.
def Patient_Profile(request):
    try:
        # Get the Patient object for the logged-in user
        patient= Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = None
    return render(request, 'hms_patient/patient_profile.html',locals())


def Book_Appointment(request):
    if not hasattr(request.user, 'patient'):
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    if request.method == 'POST':
        appointment = AppointmentForm(request.POST)
        if appointment.is_valid():
            appointment = appointment.save(commit=False)
            patient = get_object_or_404(Patient, user=request.user)
            appointment.P_ID = patient
            appointment.save()
            messages.success(request,'Appointment book successfully!!')
            appointment = AppointmentForm()
    else:
        appointment = AppointmentForm()
    return render(request, 'hms_patient/book_appointment.html',locals())



def My_Appointment(request):
    if not hasattr(request.user, 'patient'):
        return HttpResponseForbidden("You are not authorized to view this page.")
    # Get the logged-in patient's appointments
    patient = get_object_or_404(Patient, user = request.user)
    appointments = Appointment.objects.filter(P_ID=patient)
    return render(request, 'hms_patient/my_appointment.html',locals())

def Cancel_Appointment(request, appointment_id):
    if not hasattr(request.user, 'patient'):
        return HttpResponseForbidden("You are not authorized to perform this action.")

    # Get the appointment and ensure it belongs to the logged-in patient
    appointment = get_object_or_404(Appointment, Appointment_ID=appointment_id, P_ID__user=request.user)

    if appointment.Status == 'Pending':  # Allow cancel only if status is 'Pending'
        appointment.Status = 'Cancelled'
        appointment.save()
        messages.success(request, 'Your appointment has been cancelled.')
    else:
        messages.error(request, 'You can only cancel pending appointments.')
    return redirect('My_Appointment')  # Redirect to the appointments page


def Edit_Appointment(request,id):
    if not hasattr(request.user, 'patient'):
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    if request.method == 'POST':
        pi = Appointment.objects.get(pk=id)
        appointment = AppointmentForm(request.POST, instance=pi)
        if appointment.is_valid():
            appointment = appointment.save(commit=False)
            patient = get_object_or_404(Patient, user=request.user)
            appointment.P_ID = patient
            appointment.Status = 'Pending'  # Ensure the status is set to 'Pending'
            appointment.save()
            messages.success(request,'Appointment edit successfully!!')
            return HttpResponseRedirect('/hms_patient/My_Appointment/')
    else:
        pi = Appointment.objects.get(pk=id)
        appointment = AppointmentForm(instance=pi)
    return render(request, 'hms_patient/edit_appointment.html',locals())


def Edit_Patient_Profile(request):
    user = request.user  # Logged-in user
    if not user.is_patient:  # Restrict access to patients only
        return redirect('unauthorized')  # Redirect if not a patient

    patient = Patient.objects.get(user=user)  # Get the related Patient model instance

    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=user, patient=patient)
        if form.is_valid():
            form.save(user_instance=user, patient_instance=patient)
            messages.success(request,'Patient detail updated successfully!!')
            return redirect('Patient_Profile')  # Redirect to dashboard on success
    else:
        form = PatientUpdateForm(instance=user, patient=patient)
    return render(request, 'hms_patient/edit_profile.html', {'form': form})


def Doctor_List(request):
    doctor = Doctor.objects.all()
    return render(request, 'hms_patient/doctor_list.html',locals())