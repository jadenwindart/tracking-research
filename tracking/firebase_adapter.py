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
        
    def print_data(self):
        data = self.db.child("data").order_by_key().limit_to_first(10).get()
        return data.val()