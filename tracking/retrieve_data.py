from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .firebase_adapter import Firebase

# Create your views here.

class RetrieveData(APIView):

    def get(self,request):
        firebase = Firebase()
        data = firebase.get_data()
        return Response(data=data,status=status.HTTP_200_OK)


class PrintData(APIView):
          
    def get(self,request):
        firebase = Firebase()
        data1 = firebase.print_data()
        return Response(data=data1,status=status.HTTP_200_OK)