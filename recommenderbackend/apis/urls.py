from django.urls import path
from .views import (
    MovieRecommenderApi,
    SentimentApi
)

app_name = "apis"

urlpatterns = [
    path('recommender/', MovieRecommenderApi.as_view(), name="recommender"),
    path('sentiment/', SentimentApi.as_view(), name="sentiment")
]