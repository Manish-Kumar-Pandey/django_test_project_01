from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.static import static
from django.conf.urls import url
urlpatterns = [
    path('', views.home, name = "home"),
    path('signup', views.signup, name = "signup"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name = "signin"),
    path('signout', views.signout, name = "signout"),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}), 
]