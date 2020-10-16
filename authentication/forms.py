from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput({'placeholder': 'password'}))
