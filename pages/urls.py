from django.urls import path
from .views import IndexView, AboutUsView

app_name = 'pages'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutUsView.as_view(), name='about'),
]
