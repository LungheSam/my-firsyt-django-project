from django.db import models

# Create your models here.

class Room(models.Model):

    name=models.CharField(max_length=200)
    description=models.TextField(max_length=1500)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name) + ' ' + str(self.updated)