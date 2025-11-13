from django.contrib.gis.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='India')
    population = models.PositiveIntegerField(default=0)
    muslim_population = models.PositiveIntegerField(default=0)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f"{self.name}, {self.state}"
