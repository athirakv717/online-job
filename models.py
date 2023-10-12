from django.db import models

# Create your models here.
class Chat(models.Model):
    chid = models.AutoField(primary_key=True)
    chat = models.CharField(max_length=20)
    type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'chat'
