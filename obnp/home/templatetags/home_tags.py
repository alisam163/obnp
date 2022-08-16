from atexit import register
from django import template
from django.contrib.auth.models import User

register = template.Library()


menu = [
    {'title':'Главная', 'about':'home'},
    {'title':'Вакансии', 'about':'jobs'},
    {'title':'Инвестиции', 'about':'investments'},
]

@register.inclusion_tag('home/list_menu.html')
def show_menu():
    x = menu
    return {'menu':menu}