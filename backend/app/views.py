from dadata import Dadata
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from .models import Addresses

# Create your views here.

def get_dadata_geocode_address(request, source):
    dadata_token = settings.DADATA_TOKEN
    dadate_secret = settings.DADATA_SECRET

    with Dadata(dadata_token, dadate_secret) as dadata:
        dadata_result = dadata.clean(name="address", source=source)

    return JsonResponse(
        dadata_result,
        safe=False,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4,
        },
    )