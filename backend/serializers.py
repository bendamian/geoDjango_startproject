from .models import Category, Marker, Area, Polyline
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('pk', 'name')


class MarkerSerializer(GeoFeatureModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Marker
        geo_field = 'point_geom'
        fields = ('pk', 'category', 'name', 'image', 'street', 'city', 'county', 'postcode', 'active')


class AreaSerializer(GeoFeatureModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Area
        geo_field = 'boundary'
        fields = ('pk', 'category', 'name', 'boundary')


class PolylineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Polyline
        geo_field = 'path'
        fields = ('pk', 'name', 'description')