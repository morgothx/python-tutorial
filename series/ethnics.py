from django.db import models

class Ethnics(models.model):
    name: models.Charfield(max_lenght=250)
    description: models.Charfield(max_length=500)
