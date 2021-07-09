from django.urls import path, include
from .views import gallery #assasin, ryse, tomb_raider, warcraft

app_name = "gallery"

urlpatterns = [
    path('', gallery, name="index"),
    path('category/<int:pk>/', gallery, name='category'),
    # path("assasin's_creed/", assasin, name="assasin"),
    # path('ryse/', ryse, name="ryse"),
    # path('tomb_raider/', tomb_raider, name="tomb_raider"),
    # path('warcraft/', warcraft, name="warcraft"),
]
