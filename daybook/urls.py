#Define route here for daybook app


from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
#    path('home/', views.home),
    path('login/', views.login)
]

urlpatterns += staticfiles_urlpatterns()

