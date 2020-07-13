from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .firebase_adapter import Firebase

# Create your views here.

class HelloWorld(APIView):

    def get(self,request):
        data = request.data
        return Response(data="hello world"+data["input"],status=status.HTTP_200_OK)
