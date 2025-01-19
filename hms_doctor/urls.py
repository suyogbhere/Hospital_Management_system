from django.urls import path
from hms_doctor import views

urlpatterns =[
    path('doctor_profile/', views.Doctor_Profile,name='doctor_profile'),
    path('My_Appointment/', views.My_Appointment,name='Doctor_My_Appointment'),
    path('Update_Appointment/<int:id>/', views.Update_Appointment,name='Update_Appointment'),
    path('Add_Prescription/', views.Add_Prescription,name='Add_Prescription'),
    path('Search_Edit_Prescription/', views.Search_Edit_Prescription,name='Search_Edit_Prescription'),
]