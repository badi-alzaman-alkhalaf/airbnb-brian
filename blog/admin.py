from django.contrib import admin
from . import models

from django_summernote.admin import SummernoteModelAdmin
# Apply summernote to all TextField in model.
class PostAdminModel(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description',)
# Register your models here.



admin.site.register(models.Post, PostAdminModel)
admin.site.register(models.Category)
