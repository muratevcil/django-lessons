import datetime

from django.db import models
from users.models import Users
from games.models import Games


class TournamentType(models.Model):
    id = models.IntegerField(primary_key=True)
    tournamentTypeValue = models.CharField(max_length=30, null='BO1')


class Tournaments(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(Users, related_name="attended_users")
    games = models.ForeignKey(Games, related_name='games', on_delete=models.DO_NOTHING)
    begginingdate = models.DateField(null=True)
    endingdate = models.DateField(null=True)
    thumbnail = models.ImageField(null=True, blank = True , upload_to="images/")
    tournamentType = models.ForeignKey(TournamentType, related_name="tournamentType", on_delete=models.DO_NOTHING)

# Create your models here.
