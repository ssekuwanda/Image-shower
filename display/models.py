from django.db import models

# Create your models here.


class Human(models.Model):
    name = models.CharField(max_length=122)
    image = models.ImageField()

    def __str__(self):
        return self.name
