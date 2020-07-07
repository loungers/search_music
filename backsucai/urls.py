from django.urls import path
from backsucai import views


urlpatterns = [

    path('backsucai/', views.backsucai)


]