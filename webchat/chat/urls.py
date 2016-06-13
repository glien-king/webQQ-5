#!/usr/bin/env python
# encoding:utf8

from django.conf.urls import url
from chat import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^msg_sent', views.send_msg, name='send_msg'),
]