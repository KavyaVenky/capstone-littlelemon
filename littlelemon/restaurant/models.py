from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.SmallIntegerField()
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingdate = models.DateTimeField()

class Menu(models.Model):
    id = models.SmallIntegerField()
    title = models.CharField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()
