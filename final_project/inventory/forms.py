from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Device

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'phone_number', 'date_of_birth', 'position')


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'inventory_number', 'status', 'purchase_date', 'slug']
        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_inventory_number(self):
        inv_num = self.cleaned_data.get('inventory_number')
        if len(inv_num) < 4:
            raise forms.ValidationError("Инвентарный номер должен содержать не менее 4 символов.")
        return inv_num