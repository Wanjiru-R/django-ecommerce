from django.db import models
import datetime

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password= models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250, blank=True, null=True)
    price = models.DecimalField( default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='product_images/')

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField( default=0, max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(default=datetime.datetime.now)
    address = models.TextField(max_length=100, blank=True, null=True, default='No address provided')
    
    phone = models.CharField(max_length=20, default='No phone provided')
    status = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name} {self.customer.last_name}"
