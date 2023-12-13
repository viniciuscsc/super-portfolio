from django.db import models


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField()

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=False)
    github_url = models.URLField(blank=False)
    keyword = models.CharField(max_length=50, blank=False)
    key_skill = models.CharField(max_length=50, blank=False)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self) -> str:
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.URLField(blank=False)

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=False)

    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        max_length=500,
        blank=False,
    )

    timestamp = models.DateTimeField(auto_now_add=True, blank=False)

    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
        blank=False,
    )

    def __str__(self) -> str:
        return self.name
