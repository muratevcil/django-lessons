from django.db import models
from teams.models import Teams
from games.models import Games
class Users(models.Model):
    userno = models.IntegerField()
    nickname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    favorite_game = models.ForeignKey(Games,related_name='favorite_game',on_delete=models.DO_NOTHING)
    password_sha256 = models.CharField(max_length=255)
    password_raw = models.CharField(max_length=255)
    balance = models.IntegerField()
    team = models.ForeignKey(Teams, related_name='users', on_delete=models.CASCADE)
    tournaments_attendy = models.ManyToManyField('tournaments.Tournaments', related_name="attended_users")
    # tournaments_winned = models.IntegerField()
    # tournaments_win_rate = models.FloatField()
    # def __str__(self):
    #   return f"{self.name,self.surname,self.favorite_game,self.balance}"
