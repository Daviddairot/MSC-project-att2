from datetime import time
from django.db import models

class Temperatures(models.Model):
    date = models.DateField()
    time = models.TimeField(default=time(0, 0))  # Ensure this is defined
    temperature1 = models.IntegerField(null=True, blank=True, default=0)
    humidity1 = models.IntegerField(null=True, blank=True, default=0)
    temperature2 = models.IntegerField(null=True, blank=True, default=0)
    humidity2 = models.IntegerField(null=True, blank=True, default=0)
    temperature3 = models.IntegerField(null=True, blank=True, default=0)
    humidity3 = models.IntegerField(null=True, blank=True, default=0)
    temperature4 = models.IntegerField(null=True, blank=True, default=0)
    humidity4 = models.IntegerField(null=True, blank=True, default=0)
    temperature5 = models.IntegerField(null=True, blank=True, default=0)
    humidity5 = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.date} {self.time}"  # Ensure this is correct
