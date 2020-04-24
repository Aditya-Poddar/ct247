#Define route here for daybook app

from django.urls import include, path
from rest_framework import routers
from daybook import views


from django.urls import path
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
#    path('', views.index, name='index'),
#    path('home/', views.home),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.login),
    path('login1/', views.login_page),
    path('base/', views.base_page)
]

urlpatterns += staticfiles_urlpatterns()

