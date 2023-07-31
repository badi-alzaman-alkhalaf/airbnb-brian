from django.shortcuts import render
# from django.generic import ListView ,DetailView
from . import models
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import FormMixin
from .forms import PropertyReservationForm
from django.shortcuts import redirect
from django.urls import reverse
from django_filters.views import FilterView 
from . import filters
# Create your views here.
class PropertyListView(FilterView):
    model = models.Property
    filterset_class = filters.PropertyFilter
    paginate_by = 1
    template_name = 'property/property_list.html'
    
class PropertyDetailView(FormMixin, DetailView):
    model = models.Property
    form_class = PropertyReservationForm
    def get_context_data(self, **kwargs):
        context = super(PropertyDetailView, self).get_context_data(**kwargs)       
        context['related_room'] = models.Property.objects.filter(category=self.get_object().category)[:2] # type: ignore 
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            my_form = form.save(commit=False)# type: ignore  
            my_form.owner = request.user
            my_form.property = self.get_object()
            my_form.save()
            return redirect('./')