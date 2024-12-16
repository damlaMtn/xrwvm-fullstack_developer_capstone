# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    COUPE = 'Coupe'
    CONVERTIBLE = 'Convertible'
    HATCHBACK = 'Hatchback'

    CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        (COUPE, 'Coupe'),
        (CONVERTIBLE, 'Convertible'),
        (HATCHBACK, 'Hatchback'),
    ]

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=50, choices=CAR_TYPE_CHOICES)
    year = models.IntegerField()

    def clean(self):
        super().clean()
        if self.year < 2015 or self.year > 2023:
            raise ValueError("Year must be between 2015 and 2023.")

    def __str__(self):
        return f"{self.name} ({self.car_make.name})"

