from django.db import models


class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    #attendy_teams = models.ForeignKey(Tournaments, related_name="attendy_teams", on_delete=models.CASCADE)
# Create your models here.
