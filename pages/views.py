from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'pages/index.html'


class AboutUsView(TemplateView):
    template_name = 'pages/about.html'
