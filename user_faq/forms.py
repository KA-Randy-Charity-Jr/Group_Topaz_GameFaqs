from django import forms
from user_faq import models

class SignupForm(forms.ModelForm):
    displayname = forms.CharField(max_length=80)
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.GamefaqUser
        fields = ['displayname']

class GamefaqUserForm(forms.Form):
    displayname = forms.CharField(max_length=80, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)
    preferred_systems = forms.CharField(max_length=150, required=False)
    email = forms.EmailField(max_length=250, required=False)