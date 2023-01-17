from django.db import models


class expertise(models.Model):
    year = models.CharField(max_length=15)
    post = models.CharField(max_length=25)
    details = models.TextField()

class education(models.Model):
    year = models.CharField(max_length=15)
    course = models.CharField(max_length=25)
    details = models.TextField()

class skills(models.Model):
    skill = models.CharField(max_length=20)
    percentage = models.IntegerField()

class language(models.Model):
    language = models.CharField(max_length=15)
    percentage = models.IntegerField()
