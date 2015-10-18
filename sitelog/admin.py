from django.contrib import admin

# Register your models here.
from .models import sitelog

class sitelogAdmin(admin.ModelAdmin):
    list_display = ['stationID']
admin.site.register(sitelog) #register sitelog with admin
