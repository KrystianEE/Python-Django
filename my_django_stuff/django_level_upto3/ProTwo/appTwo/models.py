from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=264, unique=True)

    def __str__(self):
        temp=str(self.first_name)+' '+str(self.last_name)
        return temp
