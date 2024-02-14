from django.shortcuts import render
from .models import Category, Marker, Area, Polyline
from .serializers import CategorySerializer, MarkerSerializer, AreaSerializer, PolylineSerializer
from rest_framework import generics


# Create your views here.
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'


class MakerList(generics.ListAPIView):
    queryset = Marker.objects.all()
    serializer_class = MarkerSerializer
    name = 'maker-list'


class AreaList(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    name = 'area-list'


class PolylineList(generics.ListAPIView):
    queryset = Polyline.objects.all()
    serializer_class = PolylineSerializer
    name = 'poly-line'
