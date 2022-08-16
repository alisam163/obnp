from msilib.schema import _Validation_records
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sign-in', views.sign_in, name='signin'),
    path('registration', views.registration, name='registration'),
    path('jobs', views.jobs, name='jobs'),
    path('investments', views.investments, name='investments'),
    path('account', views.account, name='account'),
    path('logout', views.logout, name='logout')
]