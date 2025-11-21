from django.db import models
from django.conf import settings

class Listing(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    title = models.CharField(max_length=255, blank=True)
    property_type = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    price = models.CharField(max_length=50, blank=True)
    size = models.CharField(max_length=50, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    features = models.TextField(blank=True)
    condition = models.CharField(max_length=50, blank=True)
    tone = models.CharField(max_length=50)
    generated_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title or self.property_type} - {self.location}"
