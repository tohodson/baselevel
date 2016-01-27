from django.contrib import admin


# Register your models here.
#
from .models import SiteLog, Sample, Site

admin.site.register(Site)

class SamplesInline(admin.TabularInline):

    model           = Sample
    fields          = ['sample_date','comment_text']
    extra           = 24

class SampleAdmin(admin.ModelAdmin):
    #list_filter     = ['sitelog']
    #list_filter     = ['sample_date','sitelog','sitelog__station_id__site_id']
    list_filter     = ['sample_date','sitelog','sitelog__station_id']

admin.site.register(Sample, SampleAdmin)

class SiteLogAdmin(admin.ModelAdmin):

    inlines         = [SamplesInline]
    list_filter     = ['visit_date','station__site_id']


admin.site.register(SiteLog, SiteLogAdmin)

# Import-export resources
#
from import_export import resources

class SiteLogResource(resources.ModelResource):

    class Meta:
        model = SiteLog

class SiteResource(resources.ModelResource):

    class Meta:
        model = Site

