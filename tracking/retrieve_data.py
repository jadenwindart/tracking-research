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


class PaginateData(APIView):
          
    def get(self,request):
        req_data = request.data
        req_data_index = req_data["start_index"] if req_data["start_index"] != None else None
        req_data_size = req_data["size"] if req_data["size"] != None else 10
        firebase = Firebase()
        data = firebase.paginate_data(req_data_index,req_data_size)
        resp_data = {
            "meta":{
                "start_index" : req_data_index,
                "size" : req_data_size,
                "last_record" : True if len(data) < req_data_size else False
            },
            "data" : data
        }
        return Response(data=resp_data,status=status.HTTP_200_OK)