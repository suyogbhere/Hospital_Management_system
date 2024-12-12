from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from hms.managers import CustomUserManager
from hms_patient.models import *
from hms_staff.models import *
from hms_doctor.models import *

Gender_choice =(
    ('Male','Male'),
    ('Female','Female'),
)

class User(AbstractBaseUser,PermissionsMixin):
    first_name= models.CharField(max_length=250)
    last_name= models.CharField(max_length=250)
    email= models.EmailField(unique=True)
    mobile= models.CharField(max_length=10)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_patient=models.BooleanField(default=False) 
    is_doctor=models.BooleanField(default=False)
    gender = models.CharField(choices=Gender_choice,max_length=100)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile']
    object = CustomUserManager()


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    P_ID = models.AutoField(primary_key=True)
    Address = models.CharField(max_length=255, null=True)


class Department(models.Model):
    Depart_ID = models.AutoField(primary_key=True)
    Depart_Name = models.CharField(max_length=200)


room_choice = (
    ('General Ward','General Ward'),
    ('ICU','ICU'),
    ('Maternity Room','Maternity Room'),
    ('Isolation Room','Isolation Room'),
    ('Day Care Room','Day Care Room'),
    ('Delux Room','Delux Room')
)

room_status=(
    ('available','available'),
    ('occupied','occupied')
)


class Room(models.Model):
    Room_ID = models.AutoField(primary_key=True)
    P_ID = models.ForeignKey(Patient,on_delete=models.CASCADE)
    Room_no = models.IntegerField()
    Room_type = models.CharField(choices=room_choice, max_length=200)
    status = models.CharField(choices=room_status,max_length=100)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    D_ID = models.AutoField(primary_key=True)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)


payment_method_choice =(
    ('Cash','Cash'),
    ('Credit/Debit Card','Credit/Debit Card'),
    ('Mobile Wallet','Mobile Wallet'),
    ('Insurance','Insurance'),
    ('UPI','UPI')
)

class Billing(models.Model):
    Bill_ID = models.AutoField(primary_key=True)
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Total_amount = models.IntegerField()
    Pay_date = models.DateField()
    Pay_method = models.CharField(choices=payment_method_choice,max_length=100)

class Lab_Test(models.Model):
    Test_ID = models.AutoField(primary_key=True)
    P_ID = models.ForeignKey(Patient,on_delete=models.CASCADE)
    D_ID = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Test_name = models.CharField(max_length=200)
    Test_date = models.DateField()
    Test_result = models.CharField(max_length=255)

class Contact_person(models.Model):
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Contact_P = models.IntegerField()

ROLE_CHOICES = [
        ('ADMIN', 'Administrator'),
        ('DOCTOR', 'Doctor'),
        ('NURSE', 'Nurse'),
        ('RECEPTIONIST', 'Receptionist'),
        ('TECHNICIAN', 'Technician'),
        ('Medical Staff','Medical Staff'),
        ('Support Staff','Support Staff'),
    ]


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Staff_ID = models.AutoField(primary_key=True)
    Depart_ID = models.ForeignKey(Department,on_delete=models.CASCADE, null=True)
    Role = models.CharField(choices=ROLE_CHOICES, max_length=150, null=True)


Appointment_status =(
    ('Pending','Pending'),
    ('Confirmed','Confirmed'),
    ('Cancelled','Cancelled'),
    ('Rescheduled','Rescheduled'),
    ('Completed','Completed'),
    ('No-Show','No-Show')
)

class Appointment(models.Model):
    Appointment_ID = models.AutoField(primary_key=True)
    Appointment_datetime = models.DateTimeField()
    Status = models.CharField(choices=Appointment_status, max_length=255,default='PENDING')
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    D_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)

class Medicine(models.Model):
    Medicine_ID = models.AutoField(primary_key=True)
    Medicine_name = models.CharField(max_length=200)
    Cost = models.IntegerField()
    Side_effect = models.CharField(max_length=200)
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)


class Prescribed(models.Model):
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Medicine_ID = models.ForeignKey(Medicine,on_delete=models.CASCADE)


class Assigned(models.Model):
    P_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    D_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Contact(models.Model):
    fname = models.CharField(max_length=255)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
