from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,"users/index.html")

def query(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        message = request.POST['message']
        send_mail('Query', 'Hey someone asked a query on Book Area. Name - ' + str(name) + " \nEmail -  " + str(email) + "\n Message - " + message, str(email),
                  ["<Add the recievers mail id here>"], fail_silently=False)
        return HttpResponse("Query Submitted")

def logout_request(request):
    request.session['logged'] = False
    logout(request)
    messages.info(request, "Logged out successfully")
    return render(request, "users/login.html")


def login_form(request):
    if(request.session.has_key('logged')==False or request.session['logged']==False):
        return render(request, "users/login.html")
    else:
        return redirect('/areas')


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
        if len(pwd)<8:
            messages.error(request, "Password should be atleast 8 characters long.")
            return render(request,'users/register.html',{"USERNAME":username,"FNAME":fname,"LNAME":lname,"EMAIL":email,"CONTACT":mobile})
        if len(mobile)!=10 or mobile.isnumeric()==False:
            messages.error(request, "Invalid Contact Number")
            mobile=""
            return render(request,'users/register.html',{"USERNAME":username,"FNAME":fname,"LNAME":lname,"EMAIL":email,"CONTACT":mobile})
        try:
            if User.objects.get(username=username):
                messages.error(request, "This username ("+username+") already exists.")
                username=""
                return render(request,'users/register.html',{"USERNAME":username,"FNAME":fname,"LNAME":lname,"EMAIL":email,"CONTACT":mobile})
        except:
            pass
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
            request.session['logged'] = True
            messages.success(request, "Successfully Logged In ");
            return redirect('/areas')
        else:
            messages.error(request, "Invalid Credentials")
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

