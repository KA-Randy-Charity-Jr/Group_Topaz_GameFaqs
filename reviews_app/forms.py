from django import forms


class ReviewForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
    isreccomend = forms.ChoiceField(choices=[('YES','YES'),('NO','NO')])
