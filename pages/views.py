from django.views.generic import TemplateView
from utils.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    """ TemplateView for index page"""
    template_name = 'pages/index.html'
    title = 'Estate Agency'


class AboutUsView(TitleMixin, TemplateView):
    """ TemplateView for about page"""
    template_name = 'pages/about.html'
    title = 'About us'
