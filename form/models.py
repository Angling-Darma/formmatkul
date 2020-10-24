from django.db import models

# Create your models here.
class Matkul(models.Model):
    nama = models.TextField(max_length=30,default='')
    desc = models.TextField(max_length=100,default='')