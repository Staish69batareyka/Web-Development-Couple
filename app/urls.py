from django.urls import path
from . import views

urlpatterns = [
    path('track/', views.accept_package, name='accept_package'),
]