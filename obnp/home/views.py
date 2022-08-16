from xml.dom import ValidationErr
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import RegistrationUserForm
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
            print(username)
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
