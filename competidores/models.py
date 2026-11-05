from django.db import models


class Competidor(models.Model):
    nombre = models.CharField(max_length=120)
    centro = models.CharField(max_length=160)
    categoria = models.CharField(max_length=120)

    def __str__(self):
        return self.nombre