from django.db import models
from django.utils import timezone

class post(models.Model):
    title = models.CharField
    con   = models.CharField



    def __str__(self):
        return self.title

