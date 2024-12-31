from django.db import models

# Create your models here.

class AverageTime(models.Model):
    page_name = models.CharField(max_length=255)
    average_time = models.FloatField()

    def __str__(self):
        return self.page_name

class MostViewedPage(models.Model):
    page_name = models.CharField(max_length=255)
    sum_of_viewed = models.FloatField()

    def __str__(self):
        return self.page_name