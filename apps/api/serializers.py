from rest_framework.serializers import *

from apps.plane.models import Plane
from apps.flight.models import Flight
from apps.airline.models import Airline

class PlaneSerializer(ModelSerializer):

    class Meta:
        model = Plane
        fields = '__all__'

class FlightSerializer(ModelSerializer):

    class Meta:
        model = Flight
        fields = '__all__'

class AirlineSerializer(ModelSerializer):

    class Meta:
        model = Airline
        fields = '__all__'
