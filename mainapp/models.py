from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100,null=True,blank=True)
    flag_link = models.URLField(max_length=200,null=True,blank=True)
    capital = models.CharField(max_length=100,null=True,blank=True)
    largest_city = models.CharField(max_length=100,null=True,blank=True)
    official_languages = models.CharField(max_length=100,null=True,blank=True)
    area_total = models.CharField(max_length=30,null=True,blank=True)
    population = models.CharField(max_length=30,null=True,blank=True)
    gdp_nominal = models.CharField(max_length=30,null=True,blank=True)
