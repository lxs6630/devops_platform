from django.db import models

# Create your models here.
class Userinfo(models.Model):
    username=models.CharField(max_length=64)
    password=models.CharField(max_length=64)

    class Meta:
        unique_together=(('username'),)
    def __unicode__(self):
        return self.username