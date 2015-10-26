# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class WeatherRecord(models.Model):
    temperature = models.FloatField('Temperature')
    pressure = models.FloatField('Pressure')
    humidity = models.FloatField('Humidity')

    datetime = models.DateTimeField('Datetime stamp')

    class Meta:
        verbose_name = 'Weather Record'
