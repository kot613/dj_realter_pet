from django.db import models
from datetime import datetime
from agents.models import Agent


class House(models.Model):
    """
        House model for db
    """
    VERY_POOR = 1
    POOR = 2
    FAIR = 3
    BELOW_AVERAGE = 4
    AVERAGE = 5
    ABOVE_AVERAGE = 6
    GOOD = 7
    VERY_GOOD = 8
    EXCELLENT = 9
    VERY_EXCELLENT = 10

    RATES = (
        (VERY_POOR, 'Very Poor'), (POOR, 'Poor'), (FAIR, 'Fair'), (BELOW_AVERAGE, 'Below Average'),
        (AVERAGE, 'Average'), (ABOVE_AVERAGE, 'Above Average'), (GOOD, 'Good'), (VERY_GOOD, 'Very Good'),
        (EXCELLENT, 'Excellent'), (VERY_EXCELLENT, 'Very Excellent')
    )

    realtor = models.ForeignKey(Agent, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    area = models.IntegerField()
    year_build = models.IntegerField()
    total_room = models.IntegerField()
    building_type = models.CharField(max_length=255)
    overall_quality = models.SmallIntegerField(default=AVERAGE, choices=RATES)
    overall_condition = models.SmallIntegerField(default=AVERAGE, choices=RATES)

    list_date = models.DateTimeField(default=datetime.now, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.title
