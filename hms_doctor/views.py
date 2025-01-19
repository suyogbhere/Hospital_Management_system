from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from hms.models import *
from hms_doctor.models import *
from django.contrib.auth.decorators import login_required
from hms_doctor.forms import *
from django.http import HttpResponseForbidden
from django.core.paginator import Paginator


def Doctor_Profile(request):
    try:
        # Get the Patient object for the logged-in user
        doctor= Doctor.objects.get(user=request.user)
    except Doctor.DoesNotExist:
        doctor = None
    return render(request, 'hms_doctor/doctor_profile.html',locals())

def My_Appointment(request):
    if not hasattr(request.user, 'doctor'):
        return HttpResponseForbidden("You are not autherized to view this page!!")
    # Get the logged-in Doctor's appointments
    doctor = get_object_or_404(Doctor, user= request.user)
    appointments = Appointment.objects.filter(D_ID = doctor).order_by('Appointment_datetime')

     # Optional: Paginate the appointments for better UI if there are many records
    paginator = Paginator(appointments, 10)  # 10 appointments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'hms_doctor/my_appointment.html', locals())      


def Update_Appointment(request,id):
    if not hasattr(request.user, 'doctor'):
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    if request.method == 'POST':
        pi = Appointment.objects.get(pk=id)
        appointment = AppointmentForm(request.POST, instance=pi)
        if appointment.is_valid():
            appointment.save()
            messages.success(request,'Appointment update successfully!!')
            return HttpResponseRedirect('/hms_doctor/My_Appointment/')
    else:
        pi = Appointment.objects.get(pk=id)
        appointment = AppointmentForm(instance=pi)
    return render(request, 'hms_doctor/update_appointment.html',locals())


def Cancel_Appointment(request, appointment_id):
    if not hasattr(request.user, 'doctor'):
        return HttpResponseForbidden("You are not authorized to perform this action.")

    # Get the appointment and ensure it belongs to the logged-in patient
    appointment = get_object_or_404(Appointment, Appointment_ID=appointment_id, D_ID__user=request.user)

    if appointment.Status == 'Pending':  # Allow cancel only if status is 'Pending'
        appointment.Status = 'Cancelled'
        appointment.save()
        messages.success(request, 'Your appointment has been cancelled.')
    else:
        messages.error(request, 'You can only cancel pending appointments.')
    return HttpResponseRedirect('hms_doctor/My_Appointment')  # Redirect to the appointments pagedef Cancel_Appointment(request, appointment_id):
  

from django.http import JsonResponse

def Add_Prescription(request):
    if request.method =='POST':
        fm = MedicineForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Prescription added successfully !!')
    else:
       fm = MedicineForm()
    return render(request, 'hms_doctor/add_prescription.html',locals()) 

def Search_Edit_Prescription(request):
    medicines = None
    search_id = request.GET.get('P_ID', None)

    # Search for medicines based on P_ID
    if search_id:
        medicines = Medicine.objects.filter(P_ID=search_id)

    # Handle editing prescriptions
    if request.method == 'POST':
        medicine_id = request.POST.get('medicine_id')
        medicine = get_object_or_404(Medicine, pk=medicine_id)  # Fetch the medicine instance
        
        # Bind form to the existing instance
        form = MedicineForm(request.POST, instance=medicine)  
        
        if form.is_valid():
            # Save the updated data to the database
            form.save()  
            messages.success(request, 'Prescription updated successfully!')
            return redirect('Search_Edit_Prescription')  # Redirect to the same view after editing
        else:
            print(form.errors)  # Debugging: Print validation errors

    context = {
        'medicines': medicines,
        'search_id': search_id,
    }
    return render(request, 'hms_doctor/search_edit_prescription.html', context)
