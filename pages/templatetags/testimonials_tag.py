from django import template
from pages.models import Comment

register = template.Library()


@register.inclusion_tag('inc/_comments.html')
def get_comments():
    comments = Comment.objects.all()[:2]
    return {'comments': comments}
