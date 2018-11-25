from django.shortcuts import render
from django.views import View
from api.models import SensorData
import json
from rest_framework.views import APIView
from rest_framework.response import Response

class SensorDataView(APIView):
    queryset = SensorData.objects.all()
    def get(self, request, format=None):
        
        return Response(self.queryset)
