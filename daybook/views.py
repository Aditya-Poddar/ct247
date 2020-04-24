from django.shortcuts import render_to_response
from django.template import loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from daybook.serializers import UserSerializer, GroupSerializer


# Create your views here.
from django.http import HttpResponse
import daybook.models
from .models import user_attendance


def index(request):
    return HttpResponse("Hello, world. This is First Techiboy Learning Page on django. <br> <br>Do you want access of daybook app, contact admin at <b>support@abc.com</b>.")

def home(request):
    template = loader.get_template('daybook/index.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('daybook/login.html')   # getting our template
    return HttpResponse(template.render())  # rendering the template in HttpResponse
#    return HttpResponse(template.render())  # rendering the template in HttpResponse

def login_page(request):
    template = loader.get_template('daybook/login1.html')    # getting our template
    return HttpResponse(template.render())          # rendering the template in HttpResponse

def base_page(request):
    template = loader.get_template('daybook/base.html')    # getting our template
    return HttpResponse(template.render())          # rendering the template in HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]