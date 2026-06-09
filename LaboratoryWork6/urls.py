from django.urls import path
from .views import CategoryArticleListView, DeviceCreateView, DeviceUpdateView

urlpatterns = [
    path('category/<slug:category_slug>/', CategoryArticleListView.as_view(), name='category-articles'),

    path('devices/add/', DeviceCreateView.as_view(), name='device-create'),
    path('devices/<int:pk>/edit/', DeviceUpdateView.as_view(), name='device-update'),
]