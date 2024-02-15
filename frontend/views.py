from django.shortcuts import render
from django.urls import path
from .forms import AreaForm
from django.template import loader
from backend.models import Area, Marker
import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder


# Create your views here.
def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = AreaForm()
    return render(request, './forms/form.html', {'form': form})


# testing folium makers
def create_marker(request):
    data = Marker.objects.all()
    m = folium.Map(location=[51.509865, -0.118092], zoom_start=10, tiles='cartodbpositron',
                   attr='folium test markers')

    Fullscreen().add_to(m)
    LocateControl().add_to(m)
    Geocoder().add_to(m)
    folium.LatLngPopup().add_to(m)

    for d in data:
        point = [d.point_geom[1], d.point_geom[0]]

        folium.Marker(
            location=point,
            tooltip="location name: " + str(d.name),
            popup="loccation city:" + d.city,
        ).add_to(m)

    m = m._repr_html_

    map = {'m': m}
    return render(request, './pages/map_one.html', map)
