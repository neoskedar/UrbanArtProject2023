from django import forms


# Create the FormName class
class GetLocation(forms.Form):
    location = forms.CharField()
