from django.http import HttpResponse
from django.template import loader

def shop(request):
  template = loader.get_template('shop.html')
  return HttpResponse(template.render())



  