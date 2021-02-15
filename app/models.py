import datetime
import uuid
from django.db import models
from django.contrib.auth.models import User


class Staff(models.Model):
    address = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=50, null=True)
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    jobTitle = models.CharField(max_length=50)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=150)


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, null=True)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(max_length=500)
    description = models.CharField(max_length=500)
    ProductImage = models.ForeignKey('ProductImage', on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    product = models.ManyToManyField(Product, through='OrderDetails')
    status = models.CharField(max_length=10)
    paid = models.BooleanField(default=False)
    shipping_address = models.CharField(max_length=500)
    order_reference = models.UUIDField(default=uuid.uuid4)


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.RESTRICT)
    amount = models.DecimalField(decimal_places=2, max_digits=50)
    payment_reference = models.CharField(max_length=15)
    Approved = models.BooleanField(default=False)


class Feedback(models.Model):
    message = models.CharField(max_length=500)
    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)


class ProductImage(models.Model):
    file = models.ImageField(blank=False, null=False)
    name = models.CharField(max_length=20)


class OrderDetails(models.Model):
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date_crated = models.DateField(default=datetime.date.today())
