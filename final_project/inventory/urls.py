from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceListView.as_view(), name='device-list'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('items/create/', views.DeviceCreateView.as_view(), name='device-create'),
    path('items/<slug:category_slug>/', views.DeviceDetailView.as_view(), name='device-detail'),
    path('items/<slug:category_slug>/update/', views.DeviceUpdateView.as_view(), name='device-update'),
    path('items/<slug:category_slug>/delete/', views.DeviceDeleteView.as_view(), name='device-delete'),
    path('report/', views.ReportView.as_view(), name='report'),
]