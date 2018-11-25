from django.shortcuts import render
from django.views.generic import ListView
import main.models as models


class MainView(ListView):
    template_name = 'main.html'
    queryset = models.SysFunction.objects.all()
    context_object_name = 'system_funtions'

    def dispatch(self, *args, **kwargs):
            return super(MainView, self).dispatch(*args, **kwargs)
