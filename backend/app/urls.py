from django.urls import path

from . import views

urlpatterns = [
    path(
        'get_address/<str:source>/<int:distance>',
        views.get_dadata_geocode_address,
        name='showmap',
    ),
    path(
        '', views.mainpage, name='mainpage'
    ),
]
