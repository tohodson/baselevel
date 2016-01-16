from django import forms

from .models import SiteLog

class SiteLogForm(forms.ModelForm):

    class Meta:
        model = SiteLog

        fields = ('notes','personnel','visit_date', 'tape_down','logger_stage','battery_voltage','samples_taken',)
