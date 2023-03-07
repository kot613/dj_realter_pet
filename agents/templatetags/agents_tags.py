from django import template
from agents.models import Agent
from agents.forms import MessageForm

register = template.Library()


@register.inclusion_tag('inc/_best_agent_tags.html')
def get_best_agents():
    """
    Filter for agents by variables is_best='True'
    :return: QuerySEt
    """
    best_agents = Agent.objects.filter(is_best='True')
    return {'agents': best_agents}


@register.inclusion_tag('agents/mess.html')
def get_callback_form(id):
    """
    Add form callback
    """
    return {'form': MessageForm(), 'id': id}
