from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.getRecord,name='getRecord'),
    path('showInfoByCnt',views.showInfoByCnt,name='showInfoByCnt'),
]
