# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from . models import Product
# def shop(request):
#   template = loader.get_template('shop.html')
#   return HttpResponse(template.render())

def shop(request):
  products = Product.objects.all()
  return render(request, 'index.html', {'products': products})


  