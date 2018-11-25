
from django.urls import path
import instrument
import instrument.views as views

urlpatterns = [
    path("", views.InstrumentMainView.as_view(), name='instrument_main'),
    path("ig/", views.InstrumentGroupiew.as_view(), name='instrument_group'),
]
