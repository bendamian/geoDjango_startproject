from django.urls import path
from . import views

urlpatterns = [

    path('category/', views.CategoryList.as_view(), name=views.CategoryList.name),
    path('marker/', views.MakerList.as_view(), name=views.MakerList.name),
    path('area/', views.AreaList.as_view(), name=views.MakerList.name),
    path('polyline/',views.PolylineList.as_view(),name=views.PolylineList.name),

    # path('types/',views.Shop_type_view.as_view(),name=views.Shop_type_view.name),
    # path('types/<int:pk>/',views.Shop_type_detail.as_view(),name=views.Shop_type_detail.name),
    # path('markers/',views.Marker_type_view.as_view(),name=views.Marker_type_view.name),

]
