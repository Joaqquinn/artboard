from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Publicacion, Comentario, Perfil


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(label="nombre de usuario", min_length=4, max_length=150,required=True)
    email = forms.EmailField(label="correo electrónico",required=True)
    password1 = forms.CharField(label="contraseña", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label="confirma tu contraseña", widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        # Verificar si el nombre de usuario ya está registrado
        if User.objects.filter(username=username).exists():
            self.add_error("username", "El nombre de usuario ya está registrado. Por favor, elija otro.")
            

        # Verificar si el correo electrónico ya está registrado
        if User.objects.filter(email=email).exists():
            self.add_error("email", "El correo electrónico ya está registrado. Por favor, utilice otro.")

        if  password1 != password2:
            self.add_error("password1","Las contraseñas no coinciden") 
        return cleaned_data
    
    


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ["usuario"]

        fields = ["titulo", "descripcion", "estatus", "usuario", "Imagen"]


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ["comentario"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ["foto_perfil"]