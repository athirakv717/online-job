from django.db import models

# Create your models here.
class Notifications(models.Model):
    nid = models.AutoField(primary_key=True)
    notification = models.CharField(max_length=30)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'notifications'
