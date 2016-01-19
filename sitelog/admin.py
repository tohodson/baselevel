from django.contrib import admin


# Register your models here.
#
from .models import SiteLog, Sample, Site

admin.site.register(SiteLog)
admin.site.register(Sample)
admin.site.register(Site)

# Import-export resources
#
from import_export import resources

class SiteLogResource(resources.ModelResource):

    class Meta:
        model = SiteLog

class SiteResource(resources.ModelResource):

    class Meta:
        model = Site
