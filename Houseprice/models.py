from django.db import models

# Create your models here.
class Modelfeedback (models.Model):
    State: models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    pincode = models.IntegerField()
    total_sqft = models.FloatField()
    Rooms = models.IntegerField()
    bath = models.IntegerField()
    balcony = models.IntegerField()
    price = models.IntegerField()

