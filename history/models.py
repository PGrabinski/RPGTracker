from django.db import models

from django.conf import settings

class Player(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Character(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    career_path = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Session(models.Model):
    title = models.CharField(max_length=200)
    game_date = models.DateTimeField('Date played')
    description = models.CharField(max_length=2000)
    game_master = models.ForeignKey(Player, on_delete=models.CASCADE)
    xp_for_all = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Item(models.Model):
    pass