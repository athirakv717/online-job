from django.db import models

# Create your models here.
class ServiceRequest(models.Model):
    srid = models.AutoField(primary_key=True)
    service_request = models.CharField(max_length=10)
    action = models.CharField(max_length=10)
    # type = models.CharField(max_length=10)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'service_request'

