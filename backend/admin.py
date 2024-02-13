from django.contrib.gis import admin
from .models import Category, Marker, Area, Polyline

# Register your models here.
admin.site.register(Category)


class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 4,
            'default_longitude': 51.509865,
            'default_latitude': -0.118092
        }

    }


@admin.register(Marker)
class MakerAdmin(CustomGeoAdmin):
    list_display = ("name", "street", "city")


@admin.register(Area)
class AriaAdmin(CustomGeoAdmin):
    list_display = ('name', 'boundary')
    search_fields = ('name',)


@admin.register(Polyline)
class PolylineAdmin(CustomGeoAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
