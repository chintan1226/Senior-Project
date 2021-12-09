from django.db import models

# Create your models here.


class Executive(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.name
