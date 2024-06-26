from django.db import models
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User
from house_portal.models import *
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(validators = [MinLengthValidator(10), MaxLengthValidator(13)], max_length = 13)
    area = models.ForeignKey(Area, on_delete=models.PROTECT)

class Orders(models.Model):
    user = models.ForeignKey(User,  on_delete=models.PROTECT)
    # car_dealer = models.ForeignKey(CarDealer, blank=True, on_delete=models.PROTECT)
    rent = models.CharField(max_length=8)
    house = models.ForeignKey(House, on_delete=models.PROTECT, default='')
    days = models.CharField(max_length = 3)
    is_complete = models.BooleanField(default = False)
