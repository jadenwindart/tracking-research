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
        req_data_index = request.data.get("start_index")
        req_data_size = request.data.get("size") if request.data.get("size") != None else 10
        req_data_user = request.data.get("user_id")
        firebase = Firebase()
        data = firebase.paginate_data(req_data_index,req_data_size,req_data_user)
        resp_data = {
            "meta":{
                "start_index" : req_data_index,
                "size" : req_data_size,
                "last_record" : True if len(data) < req_data_size else False
            },
            "data" : data
        }
        return Response(data=resp_data,status=status.HTTP_200_OK)