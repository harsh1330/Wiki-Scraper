from django.contrib import admin
from .models import Country


class CountryListAdmin(admin.ModelAdmin):
    list_display = [
        "id", "country_name", "flag_link", "capital", "largest_city",
        "official_languages", "area_total", "population", "gdp_nominal"
    ]

    ordering = ['id']

    search_fields = ('country_name',)


admin.site.register(Country, CountryListAdmin)
