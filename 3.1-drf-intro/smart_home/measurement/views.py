
from rest_framework import generics
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorDetailSerializer, SensorListSerializer, TemperatureMeasurementSerializer

class SensorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

class SensorDetailAPIView(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorUpdateAPIView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer

class TemperatureMeasurementCreateAPIView(generics.CreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer
