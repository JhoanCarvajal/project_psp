from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from estudiantes.models import Estudiante

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields= ['username', 'email', 'first_name', 'last_name', 'password1','password2']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe prueba con otro.")
        return email

class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante
        fields = ['id_profesor']