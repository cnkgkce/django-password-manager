import django
from django.db import models


# Create your models here.


class Password(models.Model):
    key = models.CharField(max_length=30)
    password = models.BinaryField()
    username= models.CharField(max_length=20,default="noname")
    fkey = models.BinaryField()


    def __str__(self) -> str:
        return self.key