from django.db import models

class Publication(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=500)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=1000)

    def __str__(self):
        return self.name