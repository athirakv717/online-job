from django.db import models

# Create your models here.
class Photos(models.Model):
    pid = models.AutoField(primary_key=True)
    photo = models.CharField(max_length=500)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'photos'

