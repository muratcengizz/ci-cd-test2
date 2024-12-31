from django.db import models

# Create your models here.

class BrowsingData(models.Model):
    user_id = models.IntegerField()
    page_viewed = models.CharField(max_length=255)
    time_spent = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)