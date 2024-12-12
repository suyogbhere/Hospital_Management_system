from django.urls import path
from hms_staff import views

urlpatterns =[
    path('Staff_Profile/', views.Staff_Profile,name='Staff_Profile'),
]