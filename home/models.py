from django.db import models
from django.shortcuts import redirect


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    description = models.TextField()
    clientsName = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    post = models.CharField(max_length=100)
    star = models.IntegerField()

    def __str__(self):
        return self.clientsName


class Slider(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=100)
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Feature(models.Model):
    logo = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.title


LABELS = (('organic', 'organic'), ('fresh', 'fresh'), ('best', 'best'))


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    slug = models.TextField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    labels = models.CharField(max_length=100, choices=LABELS)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ('id', 'name', 'price')


class Service(models.Model):
    title = models.CharField(max_length=200)
    numbers = models.IntegerField()

    def __str__(self):
        return self.title


class Cart(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    slug = models.SlugField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ProductReviews(models.Model):
    username = models.CharField(max_length=300)
    email = models.EmailField(max_length=500)
    date = models.DateField(auto_now_add=True)
    star = models.IntegerField()
    review = models.TextField()
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.username


class Checkout(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    Address = models.CharField(max_length=100)
    phone = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    zipcode = models.IntegerField()
    description = models.TextField(blank=True)
    payment = models.CharField(max_length=200)
    def __str__(self):
        return self.firstname


