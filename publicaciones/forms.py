from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion, Comentario


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="nombre de usuario", min_length=4, max_length=150)
    email = forms.EmailField(label="correo electrónico")
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="confirma tu contraseña", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ["usuario"]

        fields = ["titulo", "descripcion", "estatus", "usuario", "Imagen"]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["comentario"]
