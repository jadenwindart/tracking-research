from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .firebase_adapter import Firebase

# Create your views here.

class DataCollector(APIView):

    def post(self,request):
        data = request.data
        firebase = Firebase()
        firebase.push_data(data)
        return Response(status=status.HTTP_200_OK)
