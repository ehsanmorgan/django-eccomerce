from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView

from .models import product


class productList(ListView):
    model=product


class productDetai(DetailView):
    model=product