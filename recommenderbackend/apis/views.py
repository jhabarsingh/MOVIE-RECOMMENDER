from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .recommender import predict as recommend
from .sentiment import predict as sentiment

class MovieRecommenderApi(APIView):
    '''
        HateSpeech Detection POST APi
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
        HateSpeech Detection POST APi
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
        
        prediction = sentiment(text)
        message = "Some error has been occured, Please Try Later"

        if prediction == 0:
            message = "no"
        else:
            message = "yes"
        data = {
            "hatespeech": prediction
        }
        return Response(data)
