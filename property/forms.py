from django import forms
from . import models

class PropertyReservationForm(forms.ModelForm):
    class Meta:
        model = models.PropertyReservation
        fields = ['date_from', 'date_to', 'guest', 'children']
    