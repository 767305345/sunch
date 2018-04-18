from django.db import models

# Create your models here.
class Whell(models.Model):
    img=models.CharField(max_length=150)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)


class Nav(models.Model):
    img=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    trackid=models.CharField(max_length=20)