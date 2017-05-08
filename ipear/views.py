from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render, redirect
#from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

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
	return render(request, "home.html")

def dispatch_overview(request):
	return render(request, "success.html")
