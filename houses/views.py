from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from utils.views import TitleMixin
from .models import House


class HousesListView(TitleMixin, ListView):
    """
    View for list houses
    """
    template_name = 'houses/list.html'
    model = House
    context_object_name = 'houses_list'
    title = 'Our Amazing Houses'


class HouseDetailView(TitleMixin, DetailView):
    """
    View for house details
    """
    template_name = 'houses/detail.html'
    model = House
    context_object_name = 'house'
    title = 'House'


def search_house(request):
    """ Search in the db from the form """
    search = None
    keyword = request.GET.get('keyword')
    city = request.GET.get('city')
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
    price = request.GET.get('price')

    if keyword:
        search = House.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))

    if city != 'All city':
        search = search.filter(city=city)

    if bedrooms != 'Any':
        search = search.filter(bedrooms=bedrooms)

    if bathrooms != 'Any':
        search = search.filter(bathrooms=bathrooms)

    if price != 'Unlimite':
        search = search.filter(price__gte=int(price))

    return render(request, 'houses/list.html', {'houses_list': search})
