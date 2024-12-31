from django.urls import path
from .views import AverageTimeAPIView, MostViewedPageAPIView

urlpatterns = [
    path("api/average-time/", AverageTimeAPIView.as_view(), name="average-time-api"),
    path("api/most-viewed/", MostViewedPageAPIView.as_view(), name="most-viewed-api"),
]