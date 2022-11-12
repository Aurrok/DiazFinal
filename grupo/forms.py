from django import forms

class BuscarBanda(forms.Form):
    nombre = forms.CharField(max_length=30, required=False)