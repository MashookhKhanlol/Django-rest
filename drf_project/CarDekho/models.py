from django.db import models
from rest_framework import serializers
from django.core.validators import MinValueValidator  , MaxValueValidator
from django.contrib.auth.models import User


def alphanumeric(value):
        if not str(value).isalnum():
            raise serializers.ValidationError("Only alphanumeric characters are allowed")
        


class Showroomlist(models.Model):
    name= models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    #ye isliye taki admin pe jab login kare tab naam dikhe na object1 2 tt

    def __str__(self):
         return self.name
    

# Create your models here.
class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length =200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100, blank=True , null=True, validators = [alphanumeric])
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    showroom = models.ForeignKey(Showroomlist,  on_delete=models.CASCADE, related_name="Showrooms", null=True)

    #This Showrooms is used inside the serializers in nested relationship

    def __str__(self):
         return self.name

class Review(models.Model):
    apiuser = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comments = models.CharField(max_length=200,null=True)
    car = models.ForeignKey(Carlist, on_delete=models.CASCADE, related_name="Reviews",null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
         return "The rating of " +self.car.name + ":--" + str(self.rating)