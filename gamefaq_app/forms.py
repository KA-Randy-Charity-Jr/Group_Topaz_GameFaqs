from django import forms
from game_app.models import Game
from console_app.models import Console


class NewGamefaq(forms.Form):
    difficulties= [('EASY','EASY'),('INTERMEDIATE','INTERMEDIATE'),('HARD','HARD')]
    title = forms.CharField(max_length=50)
   
    body = forms.CharField(widget=forms.Textarea)
    console=forms.ModelChoiceField(queryset=Console.objects.all())
    difficulty = forms.ChoiceField(choices=difficulties, required=False)
    ptype= forms.ChoiceField(choices=[('CHEATCODES','CHEATCODES'),('GAMEFAQ','GAMEFAQ')])
