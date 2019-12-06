from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserForm(UserCreationForm):
    password1 = forms.CharField(min_length=8, max_length=30, widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text = { 'username': 'Same as your Staff ID' }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Warden
        fields = '__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    