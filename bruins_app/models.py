from django.db import models

# Create your models here.

class Player_stats(models.Model):

    player_number = models.IntegerField()
    player_name = models.CharField(max_length=30)
    player_position = models.CharField(max_length=30)
    player_age = models.IntegerField()
    player_height = models.CharField(max_length=10)
    player_weight = models.IntegerField()
    shoots_catches = models.CharField(max_length=10)
    years_exp = models.IntegerField()
    birth_date = models.CharField(max_length=20)
    summary = models.CharField(max_length=20)
