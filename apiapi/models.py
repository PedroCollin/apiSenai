from django.db import models

# Create your models here.

class Question(models.Model):
    campo = models.CharField(max_length= 200)

    def __str__(self):
        return self.campo
