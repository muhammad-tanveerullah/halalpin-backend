from django.contrib.gis.db import models
from apps.core.models import City
class Listing(models.Model):
    city = models.ForeignKey(City, related_name='listings', on_delete=models.CASCADE)
    vendor = models.ForeignKey('vendors.Vendor', related_name='listings', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    halal_badge = models.CharField(max_length=30, choices=[('certified','Certified'), ('muslim_owned','Muslim Owned'), ('friendly','Halal Friendly')])
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.PointField()
    is_claimed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
