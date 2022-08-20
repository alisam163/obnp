
from django.shortcuts import render

# Create your views here.


def home(request):
    request.session['my'] = 'Green'
    print(request.session.items())
    print(request.session._SessionBase__session_key)
    return render(request, 'home/home.html')


def jobs(request):
    return render(request, 'home/jobs.html')

def investments(request):
    return render(request, 'home/investments.html')

