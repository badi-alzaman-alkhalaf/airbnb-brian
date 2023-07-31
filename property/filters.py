import django_filters
from . import models

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = models.Property
        fields = ['title', 'description', 'place', 'category']