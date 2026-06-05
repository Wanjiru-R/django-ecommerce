from django.urls import path, include
from . import views
from . views import shop

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('', shop, name='shop'),   
]