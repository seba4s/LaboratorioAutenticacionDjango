from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        # Incluimos los campos que el usuario debe llenar
        fields = ['nombre_estudiante', 'identificacion', 'asignatura', 'nota1', 'nota2', 'nota3']
        
        # El requerimiento pide excluir 'promedio' porque es automático
        widgets = {
            'nombre_estudiante': forms.TextInput(attrs={'class': 'form-control'}),
            'identificacion': forms.TextInput(attrs={'class': 'form-control'}),
            'asignatura': forms.TextInput(attrs={'class': 'form-control'}),
            'nota1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'nota2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'nota3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class LoginUsuarioForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))