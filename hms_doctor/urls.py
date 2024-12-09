from django.urls import path
from hms_doctor import views

urlpatterns =[
    path('doctor_profile/', views.Doctor_Profile,name='doctor_profile'),
]