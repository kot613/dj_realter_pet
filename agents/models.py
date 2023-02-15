from django.db import models
from datetime import datetime

from django.urls import reverse


class Agent(models.Model):
    """
        model Agent
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    photo = models.ImageField(upload_to='agents_photo/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    is_best = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MessageAgent(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    comment = models.TextField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment from {self.name}'

    def get_absolute_url(self):
        return reverse('agents:message')
