from django import forms

from .models import SiteLog, Sample

class SiteLogForm(forms.ModelForm):

    class Meta:
        model = SiteLog

        fields = ('station','personnel','visit_date', 'tape_down','logger_stage','battery_voltage','samples_taken','notes',)

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('sitelog', 'sample_date', 'comment_text')

