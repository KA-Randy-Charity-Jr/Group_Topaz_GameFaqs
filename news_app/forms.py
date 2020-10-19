from django import forms
from game_app.models import Game



class NewNewspost(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Title...'}))
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body...'}))

    

