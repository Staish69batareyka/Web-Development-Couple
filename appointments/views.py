from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('HELLO WORLD')

def appointment_list(request):
    return HttpResponse('List of all appointments')

def appointment_detail(request, appointment_id):
    return HttpResponse(f'Appointment details with ID: {appointment_id}')

def create_appointment(request):
    return HttpResponse('Appointment form')