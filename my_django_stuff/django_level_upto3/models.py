from django.db import models

# Create your models here.




class User(models.Model):
    name=models.CharField(max_length=264)
    surname=models.CharField(max_length=264)
    email=models.EmailField()

    def __str__(self):
        rtrn=str(self.name)+' '+str(self.surname)
        return str(rtrn)
