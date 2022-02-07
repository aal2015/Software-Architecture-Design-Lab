from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'display/index.html')


def button(request):
    return render(request, 'display/button.html')


def interval(request):
    return render(request, 'display/interval.html')


def displayName(request):
    return render(request, 'display/display-name.html')
