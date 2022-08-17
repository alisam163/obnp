import imp
from xml.dom import ValidationErr
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import RegistrationUserForm
from django.contrib.auth.models import User
# Create your views here.

def sign_in(request):
    return render(request, 'home/login.html')

def home(request):
    request.session['my'] = 'Green'
    print(request.session.items())
    print(request.session._SessionBase__session_key)
    return render(request, 'home/home.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            try:
                user = User.objects.create_user(username, email, password)
                user.save
            except Exception as e:
                form.add_error(None, 'Что-то пошло не так. Обратитесь к администратору')
    else:
        form = RegistrationUserForm()
    return render(request, 'home/reg.html', {'form':form})

def jobs(request):
    return render(request, 'home/jobs.html')

def investments(request):
    return render(request, 'home/investments.html')

def account():
    pass

def logout(request):
    pass
