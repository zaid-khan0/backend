
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('api/weather', views.get_weather_data, name='get_weather_data'),
]
