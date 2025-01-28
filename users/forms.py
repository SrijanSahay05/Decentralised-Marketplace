from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    wallet_address = forms.CharField(max_length=42, required=True, help_text='Required. Enter your wallet address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'wallet_address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control bg-black text-white'