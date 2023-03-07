from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from utils.views import TitleMixin
from .models import Agent, MessageAgent
from houses.models import House
from .forms import MessageForm


class AgentsListView(TitleMixin, ListView):
    """
    View for list agents
    """
    template_name = 'agents/list.html'
    model = Agent
    context_object_name = 'agents_list'
    title = 'Our agents'


class AgentsDetailView(TitleMixin, DetailView):
    """
    View for agent detail
    """
    template_name = 'agents/detail.html'
    model = Agent
    slug_url_kwarg = 'slug'
    context_object_name = 'agent'
    title = 'Agent'

    def get_context_data(self, **kwargs):
        """
        Getting a list of homes for our agent
        """
        data = super().get_context_data(**kwargs)
        data['house_list'] = House.objects.filter(realtor=self.object)
        return data


class MessageAgentCreateView(CreateView):
    """
    View for agent detail
    """
    model = MessageAgent
    form_class = MessageForm
    template_name = 'agents/mess.html'
    success_url = reverse_lazy('pages:index')

    def form_valid(self, form):
        """
        Checking the form for validity, adding data about the agent and saving the form
        """
        self.object = form.save(commit=False)
        self.object.agent = Agent.objects.get(id=form.data.get('agent_id'))
        self.object.save()

        return super(MessageAgentCreateView, self).form_valid(form)
