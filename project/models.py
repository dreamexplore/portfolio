from django.db import models

# Create your models here.

class project(models.Model):
    image = models.Imagefield(upload_to='')
    summary = models.Charfield(max_length=250)

