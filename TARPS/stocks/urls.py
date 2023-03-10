from django.urls import path

from . import views

urlpatterns = [
    path('<str:tickerID>/<str:timeLength>', views.ticker, name='ticker'),
    path('home/', views.home, name='home'),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('guide/', views.guide, name='guide'),
    path('', views.home, name='home')
]