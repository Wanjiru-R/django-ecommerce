
from django.shortcuts import render,redirect
from . models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def shop(request):
  products = Product.objects.all()
  return render(request, 'index.html', {'products': products})
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})


def login_user(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'You have been logged in.')
        return redirect('shop')
    else:
      messages.success(request, 'Invalid username or password.')
      return redirect('login')
  else:
    return render(request, 'login.html')


      
def logout_user(request):
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('shop')
  
def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('shop')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            return redirect('register')
    else:
        return render(request, 'register.html')