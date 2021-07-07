from django.shortcuts import render
from django.db import connection


# Create your views here.

def index(request):
    return render(request, '../templates/inicio.html', {})
