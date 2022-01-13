from django.db import models

# Create your models here.


class Data(models.Model):

    number=models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)
