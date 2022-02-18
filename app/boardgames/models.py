from tkinter import CASCADE
from django.db import models
from django.forms import IntegerField
from datetime import time
from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.name}"

class Boardgame(models.Model):
    name = models.CharField(max_length=200)
    player_count_max = models.IntegerField(default=100)
    player_count_min = models.IntegerField(default=1)
    release_year = models.IntegerField()
    complexity = models.FloatField()
    duration = models.IntegerField()
    bgg_link = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"

class Game(models.Model):
    date = models.DateField()
    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)
    players = models.ManyToManyField(Player, related_name="players")
    winner = models.ForeignKey(Player, on_delete=models.CASCADE)
    duration = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.boardgame} at {self.date}"

class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()

class Rating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.Case)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    rating = models.IntegerField()