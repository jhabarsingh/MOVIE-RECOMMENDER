from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .recommender import predict as recommend
from .sentiment import predict as sentiment
import json

class MovieRecommenderApi(APIView):
    '''
        Movie Recommender
    '''

    def post(self, request):
        try:
            text = request.data.get("text", None)
            if text == None:
                raise Exception("Invalid text")
            if len(text.strip()) == 0:
                raise Exception("Zero Size")
        except:
            data = {
                "message": "invalid Message"
            }
            return Response(data)

        text = text.strip()
        
        prediction = recommend(text)

        data = {
            "movies": prediction
        }
        return Response(data)


class SentimentApi(APIView):
    '''
        Movie Review Sentiment Analyser
    '''

    def post(self, request):
        try:
            text = request.data.get("text", None)
            if text == None:
                raise Exception("Invalid text")
            if len(text) == 0:
                raise Exception("Zero Size")
        except:
            data = {
                "response": "invalid Message"
            }
            return Response(data)

        
        prediction = sentiment(text)
        print(len(text))
        
        data = {
            "response": prediction
        }
        return Response(data)
