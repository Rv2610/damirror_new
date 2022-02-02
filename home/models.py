from django.db import models

class Songs(models.Model):
    song_name: models.CharField(max_length=100)

