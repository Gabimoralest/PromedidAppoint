from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

