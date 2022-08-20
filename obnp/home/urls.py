
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jobs', views.jobs, name='jobs'),
    path('investments', views.investments, name='investments'),
]