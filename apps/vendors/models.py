from django.contrib.gis.db import models
from apps.core.models import City
from django.contrib.auth import get_user_model

class Vendor(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name='vendors', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    city = models.ForeignKey(City, related_name='vendors', on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    halal_badge = models.CharField(max_length=30, choices=[('certified','Certified'), ('muslim_owned','Muslim Owned'), ('friendly','Halal Friendly')])
    is_claimed = models.BooleanField(default=False)
    location = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
