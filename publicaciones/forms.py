from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class Customcreationform(UserCreationForm):
    pass