from django.contrib import admin


# Register your models here.
#
from .models import StageRecord

admin.site.register(StageRecord)



# Import-export resources
#
from import_export import resources
from import_export import fields

class StageRecordResource(resources.ModelResource):

    # create an extra field that don't exist in the target model
    data_status = fields.Field(column_name='data_status')


    class Meta:
        model = StageRecord
        fields = ('site', )



