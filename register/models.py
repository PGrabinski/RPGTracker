from django.db import models

from django.contrib.auth.models import User

import datetime

class Player(User):
    join_date = models.DateTimeField('Join date', default=datetime.datetime.now)
    nickname = models.CharField("Nickname", max_length=50)
    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' a.k.a ' + self.nickname
