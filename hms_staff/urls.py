from django.urls import path
from hms_staff import views

urlpatterns =[
     path('Staff_Profile/', views.Staff_Profile,name='Staff_Profile'),
     path('book_room/<int:room_id>/', views.book_room, name='book_room'),
     path('Available_Rooms/', views.Available_Rooms,name='Available_Rooms'),
     path('Occupied_Rooms/', views.Occupied_Rooms,name='Occupied_Rooms'),
     path('rooms/release/<int:room_id>/', views.release_room, name='release_room'),
]