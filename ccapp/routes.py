from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('start', views.start),
    path('example', views.example),
    path('question', views.question),
    path('choose_card', views.choose_card),
    path('result', views.result),
    path('loads', views.load_json_into_db)
]