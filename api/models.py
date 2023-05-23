from msilib.schema import Class
from tokenize import blank_re
from django.db import models

# Create your models here.

class jadwal(models.Model):
    tanggal = models.CharField (max_length=20, null=False, blank=False)
    imsak   = models.TimeField (null=False, blank=False)
    subuh   = models.TimeField (null=False, blank=False)
    terbit  = models.TimeField (null=False, blank=False)
    duha    = models.TimeField (null=False, blank=False)
    zuhur   = models.TimeField (null=False, blank=False)
    asar    = models.TimeField (null=False, blank=False)
    magrib  = models.TimeField (null=False, blank=False)
    isya    = models.TimeField (null=False, blank=False)

    class Meta:
        db_table = 'jadwal'