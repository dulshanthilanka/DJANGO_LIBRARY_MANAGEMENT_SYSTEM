from django import forms
from django.contrib.auth.forms import UserCreationForm
from . models import bookdtails, userdetails

class SignupForm(UserCreationForm):
    class Meta:
        model = userdetails
        fields = ['user_name', 'user_id']
