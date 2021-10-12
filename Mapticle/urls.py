from django.urls import path

from Mapticle.views import maps_world

app_name = "Mapticle"

urlpatterns =[
    path('maps_world/', maps_world, name='maps_world')
]