from django.contrib import admin
from .models import Tournaments, TournamentType


class TournamentsAdmin(admin.ModelAdmin):
    list_display = ("id", 'name' , 'games','tournamentType')


class TournamentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'tournamentTypeValue')


admin.site.register(TournamentType, TournamentTypeAdmin)
admin.site.register(Tournaments, TournamentsAdmin)

# Register your models here.
