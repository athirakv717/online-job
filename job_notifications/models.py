from django.db import models

# Create your models here.
class JobNotifications(models.Model):
    jid = models.AutoField(primary_key=True)
    job_notification = models.CharField(max_length=20)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'job_notifications'
