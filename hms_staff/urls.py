from django.urls import path
from hms_staff import views

urlpatterns =[
    path('Staff_Profile/', views.Staff_Profile,name='Staff_Profile'),
     path('rooms/book/<int:room_id>/<int:patient_id>/', views.book_room, name='book_room'),
     path('Available_Rooms/', views.Available_Rooms,name='Available_Rooms'),
]