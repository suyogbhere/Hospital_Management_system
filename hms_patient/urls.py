from django.urls import path
from hms_patient import views

urlpatterns =[
    path('Patient_Profile/', views.Patient_Profile,name='Patient_Profile'),
    path('Book_Appointment/', views.Book_Appointment,name='Book_Appointment'),
    path('Edit_Appointment/<int:id>/', views.Edit_Appointment,name='Edit_Appointment'),
    path('My_Appointment/', views.My_Appointment,name='My_Appointment'),
    path('cancel_appointment/<int:appointment_id>/', views.Cancel_Appointment, name='cancel_appointment'),

]