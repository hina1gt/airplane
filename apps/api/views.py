from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from apps.plane.models import Plane
from apps.flight.models import Flight
from apps.airline.models import Airline
from .serializers import *


class PlaneApiView(APIView):

    def get(self, request):
        planes = Plane.objects.all()
        serializer = PlaneSerializer(planes, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = PlaneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )

class PlaneDetailApiView(APIView):

    def get(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(plane)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def patch(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        serializer = PlaneSerializer(plane, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )
        
    def delete(self, request, pk):
        plane = Plane.objects.get(pk=pk)
        plane.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )

class FlightApiView(APIView):

    def get(self, request):
        flights = Flight.objects.all()
        serializer = FlightSerializer(flights, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )

class FlightDetailApiView(APIView):

    def get(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(flight)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def patch(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        serializer = FlightSerializer(flight, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )
        
    def delete(self, request, pk):
        flight = Flight.objects.get(pk=pk)
        flight.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )
    

class AirlineApiView(APIView):

    def get(self, request):
        airlines = Airline.objects.all()
        serializer = AirlineSerializer(airlines, many=True)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def post(self, request):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )

class AirlineDetailApiView(APIView):

    def get(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        serializer = AirlineSerializer(airline)
        return Response(
            serializer.data,
            status=HTTP_200_OK
        )
    
    def patch(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        serializer = AirlineSerializer(airline, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=HTTP_201_CREATED
            )
        return Response(
                serializer.errors,
                status=HTTP_400_BAD_REQUEST
            )
        
    def delete(self, request, pk):
        airline = Airline.objects.get(pk=pk)
        airline.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )