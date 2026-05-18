from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/create/', views.create_appointment, name='create_appointments'),
    path('appointments/<int:appointment_id>', views.appointment_detail, name='appointment_detail')
]