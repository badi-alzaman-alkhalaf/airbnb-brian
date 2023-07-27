from django.shortcuts import render
# from django.generic import ListView ,DetailView
from . import models
from django.views.generic import ListView ,DetailView


# Create your views here.
class PropertListView(ListView):
    model = models.Property
    
    
class PropertyDetailView(DetailView):
    model = models.Property