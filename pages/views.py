from django.views.generic import TemplateView
from utils.views import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'pages/index.html'
    title = 'Estate Agency'


class AboutUsView(TitleMixin, TemplateView):
    template_name = 'pages/about.html'
    title = 'About us'
