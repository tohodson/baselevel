from django.db import models

# Create your models here.
class sitelog(models.Model):
    stationID = models.IntegerField()
    siteName = models.CharField(max_length=255)

    water = models.CharField(max_length=255)
    debris = models.CharField(max_length=255)


    comments = models.TextField(null=True)
    tape_Down = models.DecimalField(max_digits=6, decimal_places=3)
    stage = models.DecimalField(max_digits=6, decimal_places=3)
    #image = models.ImageField()
    #timeIn = models.DateTimeField(defualt=now)
