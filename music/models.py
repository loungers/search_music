from django.db import models


# Create your models here.


class Music(models.Model):
    # id = models.AutoField()
    name = models.CharField(max_length=255, db_column='music_name', blank=False)


class Meta:
    db_table = 'music_info'

    verbose_name = '音乐'
    verbose_name_plural = verbose_name
