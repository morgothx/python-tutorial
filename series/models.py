from django.db import models

class Serie(models.Model):
    HORROR = 'horror'
    COMEDY = 'comedy'
    ACTION = 'action'
    DRAMA = 'drama'

    CATEGORIES_CHOICES = (
        (HORROR, 'Horror'),
        (COMEDY, 'Comedy'),
        (ACTION, 'Action'),
        (DRAMA, 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

class Ethnic(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)

class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=250)
