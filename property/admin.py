from django.contrib import admin
from . import models
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class PropertyAdminModel(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description',)

# admin.site.register(SomeModel, SomeModelAdmin)


admin.site.register(models.Property, PropertyAdminModel)
admin.site.register(models.PropertyPlace)
admin.site.register(models.PropertyImages)
admin.site.register(models.PropertyRate)
admin.site.register(models.Category)
admin.site.register(models.PropertyReservation)
