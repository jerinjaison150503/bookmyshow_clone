from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('moviepage',views.moviepage)
]