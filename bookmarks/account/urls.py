from django.conf.urls import url
from django.contrib import admin
from account import views

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
]