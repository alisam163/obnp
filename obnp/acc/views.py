from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegistrationUserForm
from django.contrib.auth.models import User

# Create your views here.

def account(request):
    return HttpResponse('Аккаунт')

def login(request):
    return HttpResponse('Логин')

def registration(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            try:
                user = User.objects.create_user(username, email, password)
                user.save()
            except Exception as e:
                form.add_error(None, 'Что-то пошло не так. Обратитесь к администратору')
    else:
        form = RegistrationUserForm()
    return render(request, 'acc/reg.html', {'form':form})


def logout(request):
    return HttpResponse('logout')