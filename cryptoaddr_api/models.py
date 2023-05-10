from django.db import models
from django.utils.timezone import now

# Create your models here.
class Cryptoaddress(models.Model):
    address = models.CharField(max_length=250, null=True, blank=True)
    crypto = models.CharField(max_length=250, null=True, blank=True)
    private_key = models.CharField(max_length=250, null=True, blank=True)
    #created_at = models.DateField(default=now)

    def __str__(self):
        return self.address
