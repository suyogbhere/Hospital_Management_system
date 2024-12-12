from django.urls import path
from hms import views

urlpatterns =[
    # path('',register_user,name='register_user'),
    path('', views.Home),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact,name='contact'),
    path('register/', views.Register,name='register'),
    path('login/', views.User_Login,name='login'),
    path('patient_register/', views.Patient_Register,name='patient_register'),
    path('patient_login/', views.Patient_Login,name='patient_login'),
    path('doctor_register/', views.Doctor_Register,name='doctor_register'),
    path('doctor_login/', views.Doctor_Login,name='doctor_login'),
    path('staff_register/', views.Staff_Register,name='staff_register'),
    path('staff_login/', views.Staff_Login,name='staff_login'),
    path('logout/', views.Logout, name='logout'),
]