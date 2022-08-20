import csv

from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get('page', 1))
    with open(settings.BUS_STATION_CSV, encoding='utf8') as f:
        bus_stations = list(csv.DictReader(f))
    paginator = Paginator(bus_stations, 10)
    page = paginator.page(page_number)
    context = {
        'page': page,
        'bus_stations': bus_stations
    }
    return render(request, 'stations/index.html', context)
