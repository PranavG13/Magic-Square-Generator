from django import forms

class MagicSquareForm(forms.Form):
    size = forms.IntegerField(label="Size", min_value=3)
    sum_value = forms.IntegerField(label="Sum", min_value=15)
