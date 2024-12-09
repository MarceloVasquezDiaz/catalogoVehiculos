from .models import Vehiculo
from django.forms import ModelForm

class Add(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ["marca", "modelo", "carroceria", "motor", "categoria", "precio"]

# Usuario
from django import forms
from django.contrib.auth.models import User

class RegistroUsuario(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirmar contraseña")
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cleaned_data
