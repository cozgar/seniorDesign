from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ipear.views import (login_view, register_view, edit_view, logout_view, home, dispatch_settings_view, profile_view, staff_view, edit_user_profile_view, settings_view, edit_user_mike, edit_user_mike_edit)

urlpatterns = [
    url(r'^register/$', register_view, name='register'),
    url(r'^thankyou/$', logout_view, name='thankyou'),
    url(r'^staff/$', staff_view, name='stafflogin'),
    url(r'^login/$', login_view, name='login'),
    url(r'^profile/$', profile_view, name='profile'),
    url(r'^editprofile/$', edit_user_profile_view, name='edit_user_profile'),
    url(r'^edit_user_profile/$', edit_user_mike, name='edit_user_mike'),
    url(r'^edit_user_profile_edit/$', edit_user_mike_edit, name='edit_user_mike_edit'),
    url(r'^settings/$', settings_view, name='settings'),
    url(r'^dispatchersettings/$', dispatch_settings_view, name='dispatcher_settings'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', home, name='home'),


]
