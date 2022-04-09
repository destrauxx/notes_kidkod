from django.db import models

# Create your models here.
class Note(models.Model):
    header = models.CharField(max_length=50, null=False, blank=False)
    text = models.CharField(max_length=250, null=False, blank=True)
    status = models.BooleanField(default=False, blank=True)