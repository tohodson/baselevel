from django.db import models
from django.utils import timezone

# Create your models here.

#class Personnel
#    first_name        =
#    last_name         =
#    initials          =
#    start_date        =
#    end_date          =
#    cell_phone        =
#    work_phone        =
#    email             =


class Site( models.Model ):

    site_id           = models.IntegerField(blank=False)
    site_name         = models.CharField(max_length=100)
    waterbody_name    = models.CharField(max_length=100, blank=True)
    parent_waterbody  = models.CharField(max_length=100, blank=True)
    isws_station_code = models.CharField(max_length=100, blank=True)

    county            = models.CharField(max_length=100, blank=True)
    start             = models.DateTimeField(default=timezone.now, null=True)
    end               = models.DateTimeField(null=True, blank=True)
    road              = models.CharField(max_length=100, blank=True)

    longitude         = models.DecimalField(decimal_places=8, max_digits=11, null=True, blank=True)
    latitude          = models.DecimalField(decimal_places=8, max_digits=11, null=True, blank=True)


    nearest_town      = models.CharField(max_length=100, blank=True)
    modem_name        = models.CharField(max_length=100, blank=True)

    zipcode           = models.IntegerField(null=True, blank=True)
    modem_sn          = models.BigIntegerField(null=True, blank=True)
    ip_number         = models.CharField(max_length=100, blank=True)
    land_owner        = models.CharField(max_length=100, blank=True)

    rp_elevation      = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)
    box_rp_elevation  = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)
    d2w               = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)    # distance to water
    offset            = models.DecimalField(decimal_places=3, max_digits=6, null=True,  blank=True)

    def __str__(self):
        return str(self.site_id) + ': ' + self.site_name


class SiteLog( models.Model ):

    # log information
    personnel         = models.ForeignKey('auth.User')
    station           = models.ForeignKey(Site)
    #station           = models.IntegerField(blank=False)
    visit_date        = models.DateTimeField( default=timezone.now)
    notes             = models.TextField()

    # stage information
    tape_down         = models.FloatField(null=True, blank=True)
    logger_stage      = models.FloatField(null=True, blank=True)

    battery_voltage   = models.FloatField(null=True, blank=True)
    samples_taken     = models.IntegerField(default=0)

    def __str__(self):
        #return str(self.station.site_id) + ': ' + str(self.visit_date)
        return str(self.visit_date)


class Sample(models.Model):
    sitelog           = models.ForeignKey(SiteLog, on_delete=models.CASCADE)
    sample_date       = models.DateTimeField('collection date')
    comment_text      = models.CharField(max_length=200)

    def __str__(self):
        return str(self.sample_date)
    # XXX
    @property
    def getSite(self):
        return self.sitelog.station
    #urlparse.urlparse(self.url).hostname
    ##

