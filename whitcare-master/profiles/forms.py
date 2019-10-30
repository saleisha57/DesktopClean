from django import forms
from django.db import models
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'available_weekends', 'available_weeknights', 'rate', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

class AccountForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = { 'password': forms.PasswordInput() }
