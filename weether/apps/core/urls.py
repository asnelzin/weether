from django.conf.urls import patterns, url
from weether.apps.core.views import WeatherStat


urlpatterns = patterns(
    '',
    url(r'^$', WeatherStat.as_view(), name='main')
)