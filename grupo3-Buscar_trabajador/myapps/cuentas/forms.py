from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Perfil

# from .models import Usuario


class RegistrarUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", )


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ("foto", "descripcion", "domicilio", "numero_telefono", "categorias")
