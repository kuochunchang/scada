from django.db import models

class SysFunction(models.Model):
    id = models.CharField(max_length=40, primary_key=True)
    name = models.CharField(max_length=40)
    sequence = models.IntegerField(default=0)
    class Meta:
        ordering = ['sequence']
