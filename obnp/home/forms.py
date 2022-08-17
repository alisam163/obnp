from django import forms
from django.contrib.auth.models import User



class RegistrationUserForm(forms.Form):
    username = forms.CharField(max_length=30, label='Логин')
    email = forms.CharField(max_length=100, label='Электронная почта ')
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(), label='Повтор пароля')

