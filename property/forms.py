from django import forms
from django.utils import timezone
from .models import PropertyReservation

class PropertyReservationForm(forms.ModelForm):
    date_to = forms.DateField(widget=forms.DateInput(attrs={"id": "checkin_date"}))
    date_from = forms.DateField(widget=forms.DateInput(attrs={"id": "checkin_date"}))
    class Meta:
        model = PropertyReservation
        fields = ['date_from', 'date_to', 'guest', 'children']
    