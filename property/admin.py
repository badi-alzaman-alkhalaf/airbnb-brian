from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.Property)
admin.site.register(models.PropertyPlace)
admin.site.register(models.PropertyImages)
admin.site.register(models.PropertyRate)
admin.site.register(models.Category)
admin.site.register(models.PropertyReservation)
