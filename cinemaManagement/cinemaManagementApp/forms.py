from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CinemaDb


class TaskForm(forms.ModelForm):
    class Meta:
        model = CinemaDb
        fields = ['task', 'priority']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', )