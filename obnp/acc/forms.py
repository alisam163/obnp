from django import forms
from django.core.exceptions import ValidationError



class RegistrationUserForm(forms.Form):
    TERMS_OF_USE = (
        ('yes', ''),
    )

    username = forms.CharField(max_length=30, label='Логин')
    email = forms.CharField(max_length=100, label='Электронная почта')
    password1 = forms.CharField(min_length=6, widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(min_length=6, widget=forms.PasswordInput(), label='Повтор пароля')
    terms = forms.BooleanField()

    def clean(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise ValidationError("Пароли не совпадают. Попробуйте заново")
