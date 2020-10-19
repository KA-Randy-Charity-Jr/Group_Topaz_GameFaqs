from django import forms
from game_app.models import Game
from console_app.models import Console


class NewGamefaq(forms.Form):
    difficulties= [('', 'Difficulty...'), ('EASY','EASY'),('INTERMEDIATE','INTERMEDIATE'),('HARD','HARD')]
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Title...'}))
   
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body...'}))
    console=forms.ModelChoiceField(queryset=Console.objects.all(), empty_label='Select a console...')
    difficulty = forms.ChoiceField(choices=difficulties, required=False, )
    ptype= forms.ChoiceField(choices=[ ('', 'Type...'),('CHEATCODES','CHEATCODES'),('GAMEFAQ','GAMEFAQ')])
