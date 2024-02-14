from django.contrib.gis import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from backend.models import Area, Category


class AreaForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Area
        fields = ['category', 'name', 'boundary']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the place'}),
            'boundary': forms.OSMWidget(
                attrs={'map_width': 800, 'map_height': 500, 'default_lat': 51.509865, 'default_lon': -0.118092,
                       'default_zoom': 4}),
        }
