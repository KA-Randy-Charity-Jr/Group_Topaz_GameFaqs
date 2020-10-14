from django import forms
from game_app.models import Game
from console_app.models import Console


class NewGamefaq(forms.Form):
    difficulties= [('EASY','EASY'),('INTERMEDIATE','INTERMEDIATE'),('HARD','HARD')]
    title = forms.CharField(max_length=50)
    game = forms.ModelChoiceField(queryset=Game.objects.all(),required=False)
    body = forms.CharField(widget=forms.Textarea)
   
    difficulty = forms.ChoiceField( choices=difficulties, required=False)