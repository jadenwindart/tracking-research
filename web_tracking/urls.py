"""web_tracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tracking.retrieve_data import RetrieveData
from tracking.retrieve_data import PaginateData
from tracking.Collector_view import DataCollector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('collector', DataCollector.as_view(),name="data-collector-view"),
    path('list', RetrieveData.as_view(),name="Retrieve-Data"),
    path('list/pagination', PaginateData.as_view(),name="Print-Data")
]
