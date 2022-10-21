import folium

from dadata import Dadata
from django.conf import settings
from django.shortcuts import render

from .models import Addresses


DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


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


def add_address(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def get_dadata_geocode_address(request, source, distance):
    dadata_token = settings.DADATA_TOKEN
    dadate_secret = settings.DADATA_SECRET

    with Dadata(dadata_token, dadate_secret) as dadata:
        dadata_result = dadata.clean(
            name="address", source=source
        )

    center_point = [
        dadata_result["geo_lat"],
        dadata_result["geo_lon"]
    ]
    
    points_to_show = [center_point]
    
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

    folium_map = folium.Map(location=center_point, zoom_start=12)
    for point_to_show in points_to_show:
        add_address(
            folium_map, point_to_show[0],
            point_to_show[1]
        )

    return render(request, 'showmap.html', context={
        'map': folium_map._repr_html_(),
    })
