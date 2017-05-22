from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied
from .models import Profile
from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
	next = request.GET.get('next')
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)	
		login(request, user)

		if next:
			return redirect(next)		

		return redirect("/")

	return render(request, "login.html", {"form":form, "title": title})

def register_view(request):
	next = request.GET.get('next')
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()

		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)		
		return redirect("/")

	context = {
		"form": form,
		"title": title
	}
	return render(request, "register.html", context)

def logout_view(request):
	logout(request)
	return redirect("/")

def staff_view(request):
	return render(request, "success.html")



# this login required decorator is to not allow any view without authentication

@login_required(login_url="login/")

# Create your views here.
def home(request):
	return render(request, "dis_home.html")

def more_info_view(request):
	return render(request, "home.html")

def profile_view(request):
	return render(request, "profile.html")

def settings_view(request):
	return render(request, "settings.html")
	
def dispatch_settings_view(request):
	return render(request, "dispatcher_settings.html")

'''
def dispatch_overview(request):
	return render(request, "success.html")
'''
def edit_view(request, username):
	return render(request, "edit_profile.html")

def edit_user_profile_view(request):
	return render(request, "edit_user_profile.html")

def edit_user_mike(request):
	return render(request, "edit_user_mike.html")

def edit_user_mike_edit(request):
	return render(request, "edit_user_mike_edit.html")
'''
def edit_user(request, username):
	# querying the User object with pk from url
	user = User.objects.get(username=username)
 
	# prepopulate UserProfileForm with retrieved user values from above.
	user_form = UserRegisterForm(instance=user)
 
	# The sorcery begins from here, see explanation below
	ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('first_Name', 'last_Name', 'phone_Number', 'pets'))
	formset = ProfileInlineFormset(instance=user)
 
	if request.user.is_authenticated() and request.user.id == user.id:
		if request.method == "POST":
			user_form = UserRegisterForm(request.POST, request.FILES, instance=user)
			formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
 
		if user_form.is_valid():
			created_user = user_form.save(commit=False)
			formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)
 
		if formset.is_valid():
			created_user.save()
			formset.save()
			return HttpResponseRedirect('/')
 
		return render(request, "edit_profile.html", {"noodle": pk, "noodle_form": user_form, "formset": formset,})
	else:
		raise PermissionDenied
'''
