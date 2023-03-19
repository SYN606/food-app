from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib import messages

from .models import *

def index(request):
    return render(request, 'index.html')


def create_account(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        new_user = Create_user(
            name = name,
            email = email,
            password = password,
            phone_number = phone_number
        )

        new_user.save()

        messages.success(request, 'User Created Successfully')
        return redirect('/')
    else:
        # messages.error("Something Went Wrong. Please Try Again.!!!")
        return render(request, 'create-acc.html')

def login(request):
    return render(request, 'login.html')