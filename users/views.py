from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User


# Create your views here.

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return render(request, "users/login.html")


def login_form(request):
    return render(request, "users/login.html")


def register_form(request):
    return render(request, "users/register.html")


def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pwd = request.POST['pwd']
        mobile = request.POST['mobile']
        myuser = User.objects.create_user(username, email, pwd)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Account Created Successfullly")
        return redirect('/areas')
    else:
        return HttpResponse("404 not found")


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = authenticate(username = username, password = pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in ");
            return redirect('/areas')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('/users/login')
    else:
        return HttpResponse("404 not found")


def handleLogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "Logged out")
        return redirect('/users/login')
    else:
        return HttpResponse("404 not found")

