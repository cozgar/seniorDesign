from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ipear.views import (login_view, register_view, logout_view, home, dispatch_overview, staff_view)

urlpatterns = [
    url(r'^register/$', register_view, name='register'),
    url(r'^thankyou/$', logout_view, name='thankyou'),
    url(r'^staff/$', staff_view, name='stafflogin'),
    url(r'^login/$', login_view, name='login'),
    url(r'^dispatch/$', dispatch_overview, name='d_overview'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^', home, name='home'),


]
