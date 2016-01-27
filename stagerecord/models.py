from django.db import models

from django.utils import timezone

from sitelog.models import Site

class StageRecord(models.Model):
    site_id    = models.ForeignKey(Site)
    timestamp  = models.DateTimeField()
    stage      = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)
    discharge  = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)

    ISCO       = models.BooleanField()

    voltage    = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)
