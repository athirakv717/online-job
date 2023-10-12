from django.db import models


# Create your models here.
class Registration(models.Model):
    rid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=30)
    dob = models.DateField()
    password = models.CharField(max_length=20)

class Meta:
    managed = False
    db_table = 'registration'

