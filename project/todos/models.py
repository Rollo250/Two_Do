from django.db import models

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion=models.CharField(max_length=500)
    hora = models.TimeField()
    fecha = models.DateField()
    duracion = models.DurationField()
    completed = models.BooleanField(default=False)



"""class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)"""
