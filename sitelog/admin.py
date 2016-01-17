from django.contrib import admin

# Register your models here.
from .models import SiteLog, Sample

admin.site.register(SiteLog)
admin.site.register(Sample)
