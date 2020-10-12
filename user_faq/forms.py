from django import forms
from user_faq import models

class SignupForm(forms.ModelForm):
    displayname = forms.CharField(max_length=80)
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = models.GamefaqUser
        fields = ['displayname']