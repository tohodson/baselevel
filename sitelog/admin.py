from django.contrib import admin


# Register your models here.
#
from .models import SiteLog, Sample, Site

admin.site.register(Sample)
admin.site.register(Site)

class SamplesInline(admin.TabularInline):
    # fields = ('name','')
    model = Sample
    extra = 24

    def view_station_id(self, obj):
        return obj.station_id

    #view_station_id.

class SiteLogAdmin(admin.ModelAdmin):
    inlines = [SamplesInline]
    list_filter = ['visit_date','station__site_id']
    #list_filter = ('visit_date','station')

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
