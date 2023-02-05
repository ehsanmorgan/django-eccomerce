from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import order


class order_List(ListView):
    model=order