from django.db import models
from email.policy import default

# Create your models here.

class List(models.Model):
    itemV = models.CharField(max_length = 100)
    completed = models.BooleanField(default = False)
    
    def __str__(self):
        return self.itemV + '|'+ str(self.completed)
    