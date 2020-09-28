from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import My_User

class CreateUser(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'controls', 'placeholder': 'Digite uma senha válida'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'controls', 'placeholder': 'Repita a senha'}),
    )
    class Meta:
        model = My_User
        fields = ['first_name', 'last_name', 'username', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'controls', 'placeholder': 'Digite seu nome'}),
            'last_name': forms.TextInput(attrs={'class': 'controls', 'placeholder': 'Digite seu sobrenome'}),
            'username': forms.TextInput(attrs={'class': 'controls', 'placeholder': 'Digite seu apelido'}),
            'email': forms.TextInput(attrs={'class': 'controls', 'placeholder': 'Digite seu email'}),
        }