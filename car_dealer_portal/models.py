from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

# Create your models here.

class Area(models.Model):
    pincode = models.CharField(validators = [MinLengthValidator(6), MaxLengthValidator(6)],max_length = 6,unique=True)
    city = models.CharField(max_length = 20)

class CarDealer(models.Model):
    house_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.OneToOneField(Area, on_delete=models.PROTECT)
    wallet = models.IntegerField(default = 0)

from django.db import models

class House(models.Model):
    house_name = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=300, default="")
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    description = models.CharField(max_length=300)
    owner = models.ForeignKey(CarDealer, on_delete=models.CASCADE,  default='admin', null=True, related_name='owned_houses')  # Add ForeignKey field to represent ownership
    image = models.ImageField(upload_to='house_images/', default='')  # Add the image field

    def __str__(self):
        return self.house_name


