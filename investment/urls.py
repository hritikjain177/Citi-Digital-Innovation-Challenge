from . import views
from django.urls import path

urlpatterns = [
    
    path('sips', views.sips, name='sips'),
    path('mutualfunds', views.stocks, name='mutualfunds')
]
