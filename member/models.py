from django.db import models

# Create your models here.

class user(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    def __unicode__(self):
        return self.first_name+" "+self.last_name
class fu(models.Model):
    name=models.CharField(max_length=30)
    ufile=models.FileField(upload_to="documents/")
    def __unicode__(self):
        return self.name
