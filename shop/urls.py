from django.urls import path, include
from . import views
from . views import shop

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('', shop, name='shop'),  
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:product_id>/', views.product, name='product'),

]