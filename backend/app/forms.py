from django import forms

class AddGeoForm(forms.Form):
    address = forms.CharField(max_length=255, label="Адрес")
    radius = forms.CharField(max_length=255, label="Радиус, км")
