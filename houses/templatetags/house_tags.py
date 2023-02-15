from django import template
from houses.models import House

register = template.Library()


@register.inclusion_tag('inc/_slider.html')
def get_houses():
    houses = House.objects.order_by('-list_date')[:5]
    return {'houses': houses}


@register.inclusion_tag('inc/_search.html')
def search():
    city = ['All city'] + list(set(House.objects.values_list('city', flat=True)))
    bedrooms = ['Any'] + list(set(House.objects.values_list('bedrooms', flat=True)))
    bathrooms = ['Any'] + list(set(House.objects.values_list('bathrooms', flat=True)))
    price = ['Unlimite', 100000, 160000, 180000]

    houses = House.objects.order_by('-list_date')[:5]
    return {'houses': houses,
            'city': city,
            'bedrooms': bedrooms,
            'bathrooms': bathrooms,
            'prices': price
            }
