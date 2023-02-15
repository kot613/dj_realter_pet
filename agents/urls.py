from django.urls import path
from .views import AgentsListView, AgentsDetailView, MessageAgentCreateView

app_name = 'agents'

urlpatterns = [
    path('', AgentsListView.as_view(), name='list'),
    path('mess/to', MessageAgentCreateView.as_view(), name='message'),
    path('<slug:slug>/', AgentsDetailView.as_view(), name='detail'),

]
