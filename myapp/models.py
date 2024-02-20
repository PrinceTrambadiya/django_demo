from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    details = models.CharField(max_length=255, null=True, blank=True)