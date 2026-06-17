from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Device

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'position', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Лабораторные данные', {'fields': ('phone_number', 'date_of_birth', 'position')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Лабораторные данные', {'fields': ('phone_number', 'date_of_birth', 'position')}),
    )

class DeviceAdmin(admin.ModelAdmin):
    list_display = ['name', 'inventory_number', 'status', 'purchase_date']
    prepopulated_fields = {'slug': ('name',)}  # Слаг генерируется из имени на лету

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Device, DeviceAdmin)