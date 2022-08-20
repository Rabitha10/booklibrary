from django.db import models
from owner.models import Books
from django.contrib.auth.models import User

# Create your models here.

class Carts(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    option=(
        ("incart","incart"),
        ("cancel","cancel"),
        ("order_placed","order_placed")

    )
    status=models.CharField(max_length=120,choices=option,default="incart")

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Books,on_delete=models.CASCADE)
    delivery_address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=15)
    date=models.DateField(auto_now_add=True)
    options=(
        ("order_placed","order_placed"),
        ("dispatch","dispatch"),
        ("intransit","intransit"),
        ("delivered","delivered"),
        ("cancelled","cancelled")
    )
    status=models.CharField(max_length=120,choices=options,default="order_placed")