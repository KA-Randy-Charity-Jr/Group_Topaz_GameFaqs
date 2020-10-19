from django import forms
from user_faq import models
from user_faq.models import User_Comments, GamefaqUser


class SignupForm(forms.ModelForm):
    displayname = forms.CharField(
        max_length=80, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    username = forms.CharField(max_length=240, widget=forms.TextInput(
        attrs={'placeholder': 'displayname'}))
    password = forms.CharField(
        widget=forms.PasswordInput({'placeholder': 'password'}))

    class Meta:
        model = models.GamefaqUser
        fields = ['displayname']


class GamefaqUserForm(forms.Form):
    displayname = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = User_Comments
        fields = ['body']


class UploadPhoto(forms.ModelForm):
    class meta:
        model = GamefaqUser
        fields = ["image"]
