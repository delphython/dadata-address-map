import folium
from dadata import Dadata
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from haversine import Unit, haversine

from .forms import AddGeoForm
from .models import Addresses


def is_point_in_radius(
    point_lat,
    point_lon,
    zero_point_lat,
    zero_point_lon,
    radius
):
    return (
        haversine(
            (float(point_lat), float(point_lon)),
            (float(zero_point_lat), float(zero_point_lon)),
            unit=Unit.KILOMETERS
        ) <= radius
    )


def add_address(folium_map, lat, lon):
    folium.Marker(
        [lat, lon],
        icon=folium.Icon(color='red',icon='info-sign')
    ).add_to(folium_map)


def get_dadata_geocode_address(request, source, distance):
    dadata_token = settings.DADATA_TOKEN
    dadate_secret = settings.DADATA_SECRET

    with Dadata(dadata_token, dadate_secret) as dadata:
        dadata_result = dadata.clean(
            name='address', source=source
        )

    center_point = [
        dadata_result['geo_lat'],
        dadata_result['geo_lon']
    ]

    points_to_show = [center_point]

    if distance > 0:
        addresses = Addresses.objects.all()

        for address in addresses:
            if is_point_in_radius(
                address.geo_lat,
                address.geo_lon,
                dadata_result['geo_lat'],
                dadata_result['geo_lon'],
                distance
            ):
                points_to_show.append(
                    (
                        str(address.geo_lat),
                        str(address.geo_lon)
                    )
                )

    folium_map = folium.Map(location=center_point, zoom_start=8)
    for point_to_show in points_to_show:
        add_address(
            folium_map, point_to_show[0],
            point_to_show[1]
        )

    return render(
        request,
        'showmap.html',
        context={
            'map': folium_map._repr_html_(),
        }
    )


@csrf_exempt
def mainpage(request):
    if request.method == 'POST':
        form = AddGeoForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['address']
            radius = form.cleaned_data['radius']

            if int(radius) < 0:
                radius = 0

            return redirect(
                f'get_address/{address}/{radius}',
            )
    else:
        form = AddGeoForm()
        return render(
            request,
            'mainpage.html',
            {
                'title': 'Показать адрес',
                'form': form
            },
        )
