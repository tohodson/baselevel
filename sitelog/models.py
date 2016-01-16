from django.db import models

# Create your models here.
class SiteLog(models.Model):
    #log information
    notes = models.CharField(max_length=200)
    personnel = models.CharField(max_length=100,null=True)
    visit_date = models.DateTimeField('date published')

    #stage information
    tape_down = models.FloatField(null=True, blank=True)
    logger_stage = models.FloatField(null=True, blank=True)

    battery_voltage = models.FloatField(null=True, blank=True)
    samples_taken = models.IntegerField(default=0)

    def __str__(self):
        return self.visit_date


class Sample(models.Model):
    sitelog = models.ForeignKey(SiteLog, on_delete=models.CASCADE)
    sample_date = models.DateTimeField('collection date')
    comment_text = models.CharField(max_length=200)

    def __str__(self):
        return self.sample_date


