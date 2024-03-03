
from django.urls import path
from .views import SensorListCreateAPIView, SensorDetailAPIView, SensorUpdateAPIView, TemperatureMeasurementCreateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorDetailAPIView.as_view(), name='sensor-detail'),
    path('sensors/<int:pk>/update/', SensorUpdateAPIView.as_view(), name='sensor-update'),
    path('measurements/create/', TemperatureMeasurementCreateAPIView.as_view(), name='measurement-create'),
]
