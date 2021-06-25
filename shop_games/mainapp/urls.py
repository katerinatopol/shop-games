from django.urls import path, include
from .views import gallery, assasin, ryse, tomb_raider, warcraft


urlpatterns = [
    path('', gallery),
    path("assasin's_creed/", assasin),
    path('ryse/', ryse),
    path('tomb_raider/', tomb_raider),
    path('warcraft/', warcraft),
]
