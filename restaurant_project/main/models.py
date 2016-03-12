from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    number = models.CharField(max_length=15)
    city = models.CharField(max_length=128)
    zip_code = models.IntegerField()
    address = models.CharField(max_length=255)
    allergies = models.TextField()


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=255)
    item = models.ManyToManyField(Item)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, null=True)
    menu = models.ForeignKey(Menu, null=True)
    cuisine = models.CharField(max_length=255)
    hours = models.TextField()
    number = models.CharField(max_length=12)
    address = models.CharField(max_length=225)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(UserProfile)
    date = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
