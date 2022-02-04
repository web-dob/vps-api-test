#-*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'methodapi', views.VpsView.as_view(), name='methodapi'),
]
