from django.urls import path
from . import views

urlpatterns = [
    path('',views.GameTournaments),
    path('allTournaments/',views.AllTournaments),
    path('<int:tournamentId>/',views.TournamentDetails),
    path('newTournament/',views.NewTournament),
    path('edit/<int:tournamentId>/',views.EditTournament,name="edit_tournament"),
    path('remove/<int:tournamentId>/',views.RemoveTournament),
]