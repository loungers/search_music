from django.db import models


# Create your models here.

class useradmin(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    birth = models.DateTimeField(auto_now=True)
