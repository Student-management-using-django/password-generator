from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):

    charectors = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        charectors.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        charectors.extend(list('0123456789'))

    thepassword=""
    length=int(request.GET.get('length'))
    for x in range(length):
        thepassword+=random.choice(charectors)

    return render(request, 'generator/password.html', {"password":thepassword})

def about(request):

    return render(request, 'generator/about.html')
