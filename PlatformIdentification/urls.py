
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from PlatformIdentification import views

urlpatterns = [

   path('index', views.index, name="index"),
   path('create', views.create, name="create"),
   path('chart', views.chart, name="chart"),
   path('pchart' , views.pchart, name="pchart"),
   path('about', views.about, name="about")



]
