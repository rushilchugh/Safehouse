from django.db import models
from django.contrib.auth.admin import User


# Create your models here.


class People(models.Model):
    ip_address = models.GenericIPAddressField()
    latitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 9, decimal_places = 6)
    timezone = models.CharField(max_length = 20)
    metro_code = models.IntegerField(default = 0)
    region_code = models.CharField(max_length = 10)
    region_name = models.CharField(max_length = 20)
    country_code = models.CharField(max_length = 10)
    zip_code = models.CharField(max_length = 10)
    country_name = models.CharField(max_length = 20)
    city = models.CharField(max_length = 20)
    date_time = models.DateTimeField(auto_now_add = True)
    is_safehouse = models.BigIntegerField(default = 0)

    def __str__(self):
        return '{0} - ({1},{2})'.format(self.ip_address, self.latitude, self.longitude)


class UserProfile(User):
    mobile = models.IntegerField(max_length=12)

    def __str__(self):
        return self.user.username
