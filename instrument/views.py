from django.shortcuts import render
from django.views.generic import ListView
import instrument.models as models


class InstrumentMainView(ListView):
    template_name = 'instrument_main.html'
    context_object_name = 'groups'
    queryset = models.InstrumentGroup.objects.all()

    def dispatch(self, *args, **kwargs):
        return super(InstrumentMainView, self).dispatch(*args, **kwargs)


class InstrumentGroupiew(ListView):
    template_name = 'floor.html'
    context_object_name = 'groups'
    queryset = models.InstrumentGroup.objects.all()

    def dispatch(self, *args, **kwargs):
        return super(InstrumentGroupiew, self).dispatch(*args, **kwargs)
