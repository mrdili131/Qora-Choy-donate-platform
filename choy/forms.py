from django import forms


class AmountForm(forms.Form):
    name = forms.CharField()
    amount = forms.IntegerField()

class CardInfoForm(forms.Form):
    card = forms.CharField()
    month = forms.CharField()
    year = forms.CharField()