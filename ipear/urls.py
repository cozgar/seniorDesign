from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ipear.views import (login_view, register_view, edit_view, logout_view, home, profile_view, staff_view, settings_view)

urlpatterns = [
    url(r'^register/$', register_view, name='register'),
    url(r'^thankyou/$', logout_view, name='thankyou'),
    url(r'^staff/$', staff_view, name='stafflogin'),
    url(r'^login/$', login_view, name='login'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^edit/(?P<username>\w+)/$', edit_view, name='edit_profile'),
    url(r'^settings/$', settings_view, name='settings'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', home, name='home'),


]
