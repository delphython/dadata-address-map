from django.urls import path

from . import views

urlpatterns = [
    path(
        "get_address/<str:source>/",
        views.get_dadata_geocode_address,
        name='get_address',
    ),
]
