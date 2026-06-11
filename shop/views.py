# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render,redirect
from . models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# def shop(request):
#   template = loader.get_template('shop.html')
#   return HttpResponse(template.render())

def shop(request):
  products = Product.objects.all()
  return render(request, 'index.html', {'products': products})

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
  