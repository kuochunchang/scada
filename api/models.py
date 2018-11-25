from django.db import models

class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
