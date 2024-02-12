from django.db import models
from django.contrib.gis.db import models


# Create your models here.
# test model
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Marker(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField('location name', max_length=225, help_text=" name of the Location")
    point_geom = models.PointField()
    image = models.ImageField(upload_to='location_images/', blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Markers'

    def __str__(self):
        return f" {self.name},{self.city},{self.street},  {self.county} {self.postcode}"


class Area(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField('polygon name', max_length=225, help_text=" name of the polygon to")
    boundary = models.PolygonField()

    class Meta:
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.name
