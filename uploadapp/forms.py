
from django import forms
from .models import StudentsDeails

class StudentsDetailsForm(forms.ModelForm):
    class Meta:
        model=StudentsDeails
        fields="__all__"

class Login(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)