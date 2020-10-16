from django import forms
from game_app.models import Game



class NewNewspost(forms.Form):
    title = forms.CharField(max_length=150)
    body = forms.CharField(widget=forms.Textarea)

    

