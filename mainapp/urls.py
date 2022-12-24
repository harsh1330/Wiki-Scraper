from django.contrib import admin
from django.urls import path, include
from .views import ScraperCreateview, ScraperListDetailView, ScraperListview
urlpatterns = [
    path('country_info/', ScraperCreateview.as_view()),
    path('api/list/', ScraperListview.as_view()),
    path("api/list/<int:pk>", ScraperListDetailView.as_view()),  # Edit
]
