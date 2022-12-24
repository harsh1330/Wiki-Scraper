from rest_framework import generics, permissions
from .serializers import CountryScraperSerializer
from .models import Country
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ScraperCreateview(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryScraperSerializer


class ScraperListview(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryScraperSerializer


class ScraperListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryScraperSerializer
