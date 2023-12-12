from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name
