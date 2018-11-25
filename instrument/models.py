from django.db import models


class InstrumentGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    sequence = models.IntegerField(default=0)
    class Meta:
        ordering = ['sequence']
