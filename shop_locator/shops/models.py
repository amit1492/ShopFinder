# from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.PointField(default=Point(0, 0))

    def save(self, *args, **kwargs):
        self.location = Point(self.longitude, self.latitude, srid=4326)
        super().save(*args, **kwargs)
