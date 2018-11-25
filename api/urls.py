from django.conf.urls import url, include
from django.urls import path
import api.views as views

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path("sensordata/", views.SensorDataView.as_view(), name='sensordata'),

]
