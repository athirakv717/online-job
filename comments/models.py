from django.db import models

# Create your models here.
class Comments(models.Model):
    cmid = models.AutoField(primary_key=True)
    comment = models.CharField(max_length=60)
    service_provider = models.CharField(max_length=30)
    location = models.CharField(max_length=40)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'comments'
