from django.urls import path
from hms_patient import views

urlpatterns =[
    path('Patient_Profile/', views.Patient_Profile,name='Patient_Profile'),
]