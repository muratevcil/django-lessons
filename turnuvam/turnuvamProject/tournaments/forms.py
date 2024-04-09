from django import forms
from .models import Tournaments
class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournaments
        fields = ['id','name','begginingdate','endingdate','users','games','tournamentType','thumbnail' ]  # Add other fields as needed
        exclude=['id']

class NewTournamentForm(forms.ModelForm):
    class Meta:
        model = Tournaments
        fields = ['id','name','begginingdate','endingdate','users','games','tournamentType','thumbnail']
