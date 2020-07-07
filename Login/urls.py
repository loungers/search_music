from django.urls import path
from Login import views

urlpatterns = [
    path('login/', views.login)
]
