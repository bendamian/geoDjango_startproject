from django.urls import path
from . import views

urlpatterns = [

    path('area_form/', views.create_area, name='area_form'),

]