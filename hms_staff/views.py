from django.shortcuts import render,redirect,HttpResponseRedirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from hms.models import *
from django.contrib.auth.decorators import login_required
from hms.forms import *
from django.contrib import messages


def Staff_Profile(request):
    try:
        # Get the Staff object for the logged-in user
        staff = Staff.objects.get(user=request.user)
    except Staff.DoesNotExist:
        staff = None
    return render(request, 'hms_staff/staff_profile.html', locals())

def Available_Rooms(request):
    total_rooms = Room.objects.count()
    available_rooms = Room.objects.filter(status='available').count()
    occupied_rooms = Room.objects.filter(status='occupied').count()
    rooms = Room.objects.filter(status='available')
    patients = Patient.objects.all()  # Fetch all patients

    staff = None
    if request.user.is_authenticated:
        try:
            staff = Staff.objects.get(user=request.user)
        except Staff.DoesNotExist:
            pass  

    context = {
        'total_rooms': total_rooms,
        'available_rooms': available_rooms,
        'occupied_rooms': occupied_rooms,
        'rooms': rooms,
        'staff': staff,
        'patients': patients,  # Pass patients to the template
    }
    return render(request, 'hms_staff/room_availability.html', context)




def Occupied_Rooms(request):
    occupied_rooms = Room.objects.filter(status='occupied')
    
    context = {
        'occupied_rooms': occupied_rooms,
    }
    return render(request, 'hms_staff/room_occupied.html', context)


def book_room(request, room_id):
    room = get_object_or_404(Room, Room_ID=room_id)

    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        patient = get_object_or_404(Patient, P_ID=patient_id)

        if room.status == 'available':
            room.P_ID = patient
            room.status = 'occupied'
            room.save()
            messages.success(request, f"Room {room.Room_no} booked for {patient.P_Name}")
        else:
            messages.error(request, "Room is already occupied")

    return redirect('available_rooms')



def release_room(request, room_id):
    room = get_object_or_404(Room, Room_ID=room_id)

    if room.status == 'occupied':
        room.P_ID = None
        room.status = 'available'
        room.save()
        messages.success(request, f"Room {room.Room_no} is now available")
    else:
        messages.error(request, "Room is already available")

    return redirect('Available_Rooms')


