from django.shortcuts import render
from django.urls import path
from .forms import AreaForm
from django.template import loader
from backend.models import Area


# Create your models here.

def create_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else
    else:
        form = AreaForm()
    return render(request, './forms/form.html', {'form': form})

# Create your views here.
