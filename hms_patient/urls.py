from django.urls import path
from hms_patient import views


urlpatterns =[
    path('Patient_Profile/', views.Patient_Profile,name='Patient_Profile'),
    path('Book_Appointment/', views.Book_Appointment,name='Book_Appointment'),
    path('Edit_Appointment/<int:id>/', views.Edit_Appointment,name='Edit_Appointment'),
    path('My_Appointment/', views.My_Appointment,name='Patient_My_Appointment'),
    path('cancel_appointment/<int:appointment_id>/', views.Cancel_Appointment, name='cancel_appointment'),
    path('edit_profile/',views.Edit_Patient_Profile,name='edit_patient_profile'),
    path('Doctor_List/',views.Doctor_List,name='Doctor_List')

]