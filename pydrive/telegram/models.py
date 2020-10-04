from django.db import models


# Create your models here.

class dataset(models.Model):
    firstname = models.TextField()
    lastname = models.TextField()
    nid = models.TextField()
    mobile = models.TextField()
    

def __str__(self):
    return self.mobile