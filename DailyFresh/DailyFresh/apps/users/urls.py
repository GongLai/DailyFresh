#!/usr/bin/python3
# -*- coding: utf-8 -*-
from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='register'),  # 用户注册
]
