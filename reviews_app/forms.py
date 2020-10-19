from django import forms


class ReviewForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Body...'}))
    isreccomend = forms.ChoiceField(choices=[('', 'Would you reccomend?'),('YES','YES'),('NO','NO')])
