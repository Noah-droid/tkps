from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User

class Area(models.Model):
    pincode = models.CharField(
        validators=[MinLengthValidator(6), MaxLengthValidator(6)],
        max_length=6,
        unique=True
    )
    city = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.city} ({self.pincode})"

class Owner(models.Model):
    house_owner = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(
        validators=[MinLengthValidator(10), MaxLengthValidator(13)], 
        max_length=13
    )
    area = models.OneToOneField(Area, on_delete=models.PROTECT)
    wallet = models.IntegerField(default=0)

    def __str__(self):
        return self.house_owner.username

TYPE_CHOICES = [
    ('House', 'House'),
    ('Hostels', 'Hostels'),
    ('Hotel', 'Hotel'),
    ('Restaurant', 'Restaurant'),
]

class House(models.Model):
    name = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
    mail = models.EmailField(default='', null=True, blank=True)
    phone = models.CharField(max_length=20, default="", null=True, blank=True)
    address = models.CharField(max_length=300, default="")
    bedrooms = models.PositiveIntegerField(null=True, blank=True)
    bathrooms = models.PositiveIntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    type = models.CharField(
        max_length=20, 
        choices=TYPE_CHOICES, 
        default='House'  # Changed the default to a valid choice
    )
    description = models.TextField(max_length=1000)  # Increased the max_length for more flexibility
    is_student_only = models.BooleanField(default=True)
    owner = models.ForeignKey(
        Owner, 
        on_delete=models.CASCADE,  
        null=True, 
        related_name='owned_houses'
    )
    image = models.ImageField(upload_to='house_images/', default='', blank=True) 
    # Added blank=True for flexibility in form submissions
     # Added blank=True for flexibility in form submissions

    def __str__(self):
        return self.name
