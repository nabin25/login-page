from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import myapp


def home(request):
    return render(request, 'myapp/home.html')


def ui(request):
    return render(request, 'myapp/ui.html')
