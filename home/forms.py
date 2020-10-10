from django import forms
from home.models import Game

class GameForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    instructions = forms.CharField(max_length=50)
    timereq = forms.CharField(max_length=50)