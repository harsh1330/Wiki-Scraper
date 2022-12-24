from rest_framework import serializers
from .models import Country
from .wiki_scraper import BusinessLogicService


class CountryScraperSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Country
        fields = ("id", "country_name", "flag_link", "capital", "largest_city",
                  "official_languages", "area_total", "population", "gdp_nominal")
        read_only_fields = ("id", "flag_link", "capital", "largest_city",
                            "official_languages", "area_total", "population", "gdp_nominal")

    def create(self, validated_data):
        # print(validated_data, type(validated_data))
        business_logic_data = BusinessLogicService(
        ).do_some_logical_ops(validated_data["country_name"])
        return Country.objects.create(**business_logic_data)
