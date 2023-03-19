from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'index.html')


def create_account(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['f_name']
        last_name = request.POST['l_name']
        email = request.POST['email']
        password_1 = request.POST['password-1']
        password_2 = request.POST['password-2']
        phone_number = request.POST['phone_number']


        if password_1 == password_2:
            new_user = User.objects.create_user(username, email, password_1)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()

            messages.success(request, 'User Created Successfully')

        else:
            messages.error(request, 'password did not match please try again')

        return redirect('/')
    else:
        # messages.error("Something Went Wrong. Please Try Again.!!!")
        return render(request, 'create-acc.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']

        print(username, password)
        user = authenticate(
                            username = username, 
                            password = password
                            )

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def user_logout(request):
    logout(request)
    return redirect('/')