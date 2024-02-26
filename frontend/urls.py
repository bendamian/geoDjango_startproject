from django.urls import path
from . import views

urlpatterns = [

    path('area_form/', views.create_area, name='area_form'),
    path('marker_map', views.create_marker, name='marker_map'),
    path('map_claster/', views.create_marker_cluster, name='map_claster'),
    path('polyline/',views.create_polyline, name='polyline'),
    path('world/',views.create_world,name='world')

]