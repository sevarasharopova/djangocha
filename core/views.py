from django.shortcuts import render

from frontend import *

def atirgul(request):
    return render(request,'atirgul.html')

def liliya(request):
    return render(request,'liliya.html')

def lola(request):
    return render(request,'lola.html')

def moychechak(request):
    return render(request,'moychechak.html') 
