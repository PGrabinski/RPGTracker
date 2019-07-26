from django.db import models

from django.contrib.auth.models import User

from django.conf import settings

import datetime

class Player(User):
    join_date = models.DateTimeField('Join date', default=datetime.datetime.now)
    nickname = models.CharField("Nickname", max_length=50)
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' a.k.a ' + self.nickname

class Character(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Player')
    name = models.CharField(max_length=200)
    creation_date = models.DateTimeField('Creation date', default=datetime.datetime.now)

    story = models.CharField(default='Once upon a time...', max_length=5000)

    career_path = models.CharField(max_length=50)
    career_level = models.PositiveIntegerField(default=1)

    total_xp = models.IntegerField(default=0)
    spent_xp = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name + ', ' + self.career_path
    models.Model.save

class Session(models.Model):
    title = models.CharField('Title',max_length=200)
    game_date = models.DateTimeField('Date played', default=datetime.datetime.now)
    description = models.CharField(max_length=2000)
    game_master = models.ForeignKey(Player, on_delete=models.CASCADE)
    xp_for_all = models.IntegerField('Experience for all players', default=0)
    characters = models.ManyToManyField(Character, related_name='characters')

    def __str__(self):
        return self.title

class Item(models.Model):
    pass