from django.db import models

# Create your models here.


class Executive(models.Model):
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    ticker = models.CharField(max_length=10)
    description = models.TextField(max_length=300)
    following = models.IntegerField()
    followers = models.IntegerField()

    def __str__(self):
        return self.name
