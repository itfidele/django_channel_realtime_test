from django.db import models
import uuid

# Create your models here.


class Data(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    number=models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)
