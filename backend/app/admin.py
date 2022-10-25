from django.contrib import admin

from .models import Addresses

# Register your models here.

@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    pass
