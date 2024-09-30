from django.db import models
from django.contrib.auth.models import User

from django.db import models

class RentalItem(models.Model):
    CATEGORY_CHOICES = [
        ('laptop', 'Laptop'),
        ('camera', 'Camera'),
        ('tablet', 'Tablet'),
        # Add more categories as needed
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='laptop')
    description = models.TextField()
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='rental_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.category})'


from datetime import timedelta

class Rental(models.Model):
    item = models.ForeignKey(RentalItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.item.name} rented by {self.user.username}'

    @property
    def rental_duration(self):
        if self.return_date:
            return (self.return_date - self.rental_date).days
        return None

    @property
    def total_rental_cost(self):
        if self.return_date:
            duration = self.rental_duration or 0
            return duration * self.item.rental_price
        return None
    
    def save(self, *args, **kwargs):
        if not self.return_date:
            self.item.is_available = False
        else:
            self.item.is_available = True
        self.item.save()
        super(Rental, self).save(*args, **kwargs)

