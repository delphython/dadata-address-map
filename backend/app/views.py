from dadata import Dadata
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .models import Addresses

# Create your views here.

def is_point_in_radius(
    point_lat,
    point_lon,
    zero_point_lat,
    zero_point_lon,
    radius
):
    return (
        (float(point_lat) - float(zero_point_lat))**2
        + (float(point_lon) - float(zero_point_lon))**2
        <= radius**2
    )


def get_dadata_geocode_address(request, source, distance):
    dadata_token = settings.DADATA_TOKEN
    dadate_secret = settings.DADATA_SECRET

    with Dadata(dadata_token, dadate_secret) as dadata:
        dadata_result = dadata.clean(
            name="address", source=source
        )
    
    points_to_show = [
        (
            dadata_result["geo_lat"],
            dadata_result["geo_lon"]
        )
    ]
    
    if distance > 0:
        addresses = Addresses.objects.all()

        for address in addresses:
            if is_point_in_radius(
                address.geo_lat,
                address.geo_lon,
                dadata_result["geo_lat"],
                dadata_result["geo_lon"],
                distance
            ):
                points_to_show.append(
                    (
                        str(address.geo_lat),
                        str(address.geo_lon)
                    )
                )

    print(points_to_show)

    return JsonResponse(
        dadata_result,
        safe=False,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4,
        },
    )
