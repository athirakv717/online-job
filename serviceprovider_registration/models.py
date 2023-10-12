from django.db import models
from service_request.models import ServiceRequest
# Create your models here.
class SrRegistration(models.Model):
    spid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    dob = models.DateField()
    typeofservice = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    # srid = models.IntegerField()
    s=models.ForeignKey(ServiceRequest,on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'sr_registration'


