from django.shortcuts import render
from django.urls import path
from .forms import AreaForm
from django.template import loader
from backend.models import Area, Marker,Polyline
import folium
from folium.plugins import MarkerCluster, Fullscreen, LocateControl, Geocoder
from django.core.serializers import serialize
import json


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
    
    m2 = folium.Map(location=[51.509865, -0.118092], zoom_start=10, tiles='cartodbpositron',
                   attr='folium poly line ')

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

    m = m._repr_html_()
    m2 = m2._repr_html_()

    map = {'m': m,'n':m2}
    return render(request, './pages/map_one.html', map)


# Testing a function returns marker cluster using folium
def create_marker_cluster(request):

    data = Marker.objects.all()

    map = folium.Map(
        location=[51.509865, -0.118092],
        tiles='cartodbpositron',
        zoom_start=7,
        attr='Folium test cluster'
    )

    marker_cluster = MarkerCluster()

    for d in data:
        point= [d.point_geom[1], d.point_geom[0]]
        marker_cluster.add_child(
            folium.Marker(
                location=point,
                tooltip="location Name: " + str(d.name),
                popup="location city :" + d.city,
            )
        )

    map.add_child(marker_cluster)
    
    Fullscreen().add_to(map)
    LocateControl().add_to(map)
    Geocoder().add_to(map)
    folium.LatLngPopup().add_to(map)

    map = map._repr_html_()

    context = {'map': map}

    return render(request, './pages/map_claster.html', context)




# testing folium polyline
def create_polyline(request):
    url = 'http://127.0.0.1:5001/backend/polyline/'
    url2='http://127.0.0.1:5001/backend/area/'
    #geojason = serialize("geojson", Polyline.objects.all(), geometry_field= "LineString", fields=["path","name","description "])
   

    m = folium.Map(location=[51.509865, -0.118092], zoom_start=10, tiles='cartodbpositron',
                   attr='folium poly line ')
                   
    
    folium.GeoJson(url,name="path").add_to(m)
    folium.GeoJson(url2,name="area").add_to(m)

    folium.LayerControl().add_to(m)


   
    Fullscreen().add_to(m)
    LocateControl().add_to(m)
    Geocoder().add_to(m)
    folium.LatLngPopup().add_to(m)

    m = m._repr_html_()

    map = {'m': m}
    return render(request, './pages/polyline.html', map)




#whole world map
def create_world(request):
    #url = 'http://127.0.0.1:5001/backend/marker/'
    
    data = Marker.objects.all()
    
 

    m = folium.Map(location=(30, 10), zoom_start=3 ,tiles='cartodbpositron',
                   attr='world map testing ')
                   
    
    #folium.GeoJson(url,name="points").add_to(m)
    
    for d in data:
        point = [d.point_geom[1], d.point_geom[0]]

        folium.Marker(
            location=point,
            tooltip="location name: " + str(d.name),
            popup="loccation city:" + d.city,
            icon=folium.Icon(color='green', prefix='fa',icon='bicycle')
        ).add_to(m)
    
  

    folium.LayerControl().add_to(m)
    


   
    Fullscreen().add_to(m)
    LocateControl().add_to(m)
    Geocoder().add_to(m)
    folium.LatLngPopup().add_to(m)

    m = m._repr_html_()

    map = {'m': m}
    return render(request, './pages/world.html', map)