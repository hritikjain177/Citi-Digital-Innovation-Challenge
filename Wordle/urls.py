from . import views
from django.urls import path

urlpatterns = [
    path('wordle', views.wordle, name='wordle'),
]
