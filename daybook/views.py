#from django.shortcuts import render_to_response
from django.template import loader

# Create your views here.
from django.http import HttpResponse
import daybook.models


def index(request):
    return HttpResponse("Hello, world. This is First Techiboy Learning Page on django.")

def home(request):
    template = loader.get_template('daybook/index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('daybook/login.html')    # getting our template
    return HttpResponse(template.render())          # rendering the template in HttpResponse