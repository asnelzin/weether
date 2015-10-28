from __future__ import unicode_literals

from datetime import datetime

from django.views.generic import ListView
from weether.apps.core.models import WeatherRecord


class WeatherStat(ListView):
    model = WeatherRecord
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(WeatherStat, self).get_context_data(**kwargs)
        context.update({'today_data': WeatherRecord.objects.filter(datetime__gte=datetime.date(datetime.now()),
                                                                   datetime__lte=datetime.now()).order_by('datetime'),
                        'latest': WeatherRecord.objects.latest('pk')})
        return context