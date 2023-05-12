from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def sayHello(request):
    tmp = loader.get_template('user.html')
    return HttpResponse(tmp.render())

# Create your views here.
