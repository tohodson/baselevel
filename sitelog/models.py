from django.db import models
from django.utils import timezone

# Create your models here.
class SiteLog(models.Model):
    #log information
    personnel = models.ForeignKey('auth.User')
    visit_date = models.DateTimeField( default=timezone.now)
    notes = models.TextField()

    #stage information
    tape_down = models.FloatField(null=True, blank=True)
    logger_stage = models.FloatField(null=True, blank=True)

    battery_voltage = models.FloatField(null=True, blank=True)
    samples_taken = models.IntegerField(default=0)

    #def __str__(self):
    #    return print(self.visit_date)


class Sample(models.Model):
    sitelog = models.ForeignKey(SiteLog, on_delete=models.CASCADE)
    sample_date = models.DateTimeField('collection date')
    comment_text = models.CharField(max_length=200)

    #def __str__(self):
    #    return print(self.sample_date)


