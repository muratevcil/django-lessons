from django.http import HttpResponse
from django.template import loader
from tournaments.models import Tournaments, TournamentType
from games.models import Games
from django.shortcuts import render, redirect
from .forms import TournamentForm
from django.core.files.storage import FileSystemStorage
from .forms import TournamentForm,NewTournamentForm
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions

from django.shortcuts import render, redirect, get_object_or_404
from .forms import TournamentForm  # Replace with the actual import path for your TournamentForm
from .models import Tournaments  # Replace with the actual import path for your Tournaments model

def GameTournaments(request, gameId):
    gameTournaments = Tournaments.objects.filter(games_id=gameId).values()
    asset = loader.get_template('gametournaments.html')
    data = {
        'gameTournaments': gameTournaments,
    }
    print(gameTournaments)
    return HttpResponse(asset.render(data, request))


def AllTournaments(request):
    gameTournaments = Tournaments.objects.all().values()
    asset = loader.get_template('gametournaments.html')
    data = {
        'gameTournaments': gameTournaments
    }
    return HttpResponse(asset.render(data, request))


def TournamentDetails(request, tournamentId):
    tournamentInstance = Tournaments.objects.get(id = tournamentId)
    tournamentDetails = Tournaments.objects.filter(id=tournamentId).values()
    tournamentTypes = TournamentType.objects.filter(id=tournamentDetails[0]["tournamentType_id"]).values()
    games = Games.objects.filter(id=tournamentDetails[0]["games_id"]).values()
    users = tournamentInstance.users.all()
    thumbnail = tournamentInstance.thumbnail
    asset = loader.get_template('details.html')
    data = {
        'tournamentDetails': tournamentDetails,
        'tournamentTypes': tournamentTypes,
        'games':games,
        'users':users,
        'thumbnail':thumbnail
    }
    print(tournamentDetails)
    return HttpResponse(asset.render(data, request))


def NewTournament(request):
    hatalar = []
    profilResmi_url = ""
    profilResmi = request.FILES.get('thumbnail', False)  # Change 'profil' to 'thumbnail'
    tournaments = Tournaments.objects.values()

    if profilResmi:
        try:
            # Check if the file is a valid image
            get_image_dimensions(profilResmi)
        except (IOError, ValidationError):
            hatalar.append("The file you uploaded is either not an image or a corrupted image.")
        else:
            fs = FileSystemStorage()
            yukle = fs.save('images/' + profilResmi.name, profilResmi)
            profilResmi_url = fs.url(yukle)
    else:
        hatalar.append("Thumbnail cannot be empty.")
    print(profilResmi_url)
    if request.method == 'POST':
        form = NewTournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.thumbnail = profilResmi_url
            print(profilResmi_url)
            print(tournament)
            print(tournament.thumbnail)
            tournament.save()
            form.save_m2m()  # Save the many-to-many relationships, like users
            return redirect('/tournaments/allTournaments')
        else:
            print(form.errors)  # Print form errors to console for debugging
    else:
        form = NewTournamentForm()

    return render(request, 'new_tournament.html', {'form': form, 'tournaments': tournaments})



def EditTournament(request, tournamentId):
    # Retrieve the tournament instance
    tournament_instance = get_object_or_404(Tournaments, id=tournamentId)

    if request.method == 'POST':
        # Pass the form data and files to the TournamentForm
        form = TournamentForm(request.POST, request.FILES, instance=tournament_instance)
        if form.is_valid():
            # Save the form data to the existing instance
            tournament = form.save(commit=False)
            fs = FileSystemStorage()
            fs.save('images/' + str(tournament.thumbnail),tournament.thumbnail)
            tournament.thumbnail = "/media/images/" + str(tournament.thumbnail)
            tournament.save()
            print("Form saved successfully.")
            return redirect('/tournaments/allTournaments')
        else:
            print("Form is not valid. Errors:", form.errors)  # Print form errors to the console for debugging
    else:
        # Pass the existing instance to the form for editing
        form = TournamentForm(instance=tournament_instance)

    return render(request, 'edit.html', {'form': form, 'tournamentId': tournament_instance.id})



def RemoveTournament(request,tournamentId):
    removingTournamentObject = Tournaments.objects.filter(id = tournamentId)
    removingTournamentObject.delete()
    return redirect("anasayfa")
