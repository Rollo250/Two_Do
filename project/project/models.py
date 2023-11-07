from django.db import models

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        app_label = 'project'