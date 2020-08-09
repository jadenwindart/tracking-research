import pyrebase
from tracking.config.firebase import firebase_config

class Firebase:  
    
    def __init__(self):
        firebase = pyrebase.initialize_app(firebase_config)
        self.db = firebase.database()

    def push_data(self,recv_data={}):
        data = {
            "user_id" : recv_data['user_id'],
            "mnc" : recv_data['mnc'],
            "mcc" : recv_data['mcc'],
            "radio" : recv_data['radio'],
            "timestamp" : recv_data['timestamp'],
            "cells": [{
                "cellid" : x["cell_id"],
                "rss" : x["rss"]
            } for x in recv_data["cells"]],
            "lat" : recv_data["lat"],
            "lon" : recv_data["lon"]
        }
        self.db.child("data").push(data)
        
    def get_data(self):
        data = self.db.child("data").get()
        return data.val()
        
    def paginate_data(self,data_index,number_retrieve,user_id=None):
        query = self.db.child("data")
        if( user_id != None):
            query = query.order_by_child("user_id").equal_to(user_id)
        else:
            query = query.order_by_key()

        if(data_index != None and user_id == None):
            query = query.start_at(data_index).limit_to_first(number_retrieve).get()
        else:
            query = query.limit_to_first(number_retrieve).get()
        records = query.val()
        data = []
        for record in records:
            data.append({
                "record_id" : record,
                "user_id" : records[record]['user_id'],
                "mnc" : records[record]['mnc'],
                "mcc" : records[record]['mcc'],
                "radio" : records[record]['radio'],
                "timestamp" : records[record]['timestamp'],
                "cells": [{
                    "cellid" : x["cellid"],
                    "rss" : x["rss"]
                } for x in records[record]["cells"]],
                "lat" : records[record]["lat"],
                "lon" : records[record]["lon"]
            })
        return data