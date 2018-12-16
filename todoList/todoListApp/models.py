from django.db import models
from email.policy import default

# Create your models here.

class List(models.Model):
    itemV = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)
    priority = models.PositiveSmallIntegerField(default = 0)
    autor =  models.CharField(max_length = 100,default = "")
    filter = models.BooleanField(default = True)
    
    def __str__(self):
        return self.itemV + '|'+ str(self.completed)
    