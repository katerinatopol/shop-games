from django.db import models

from shop_games import settings
from mainapp.models import Games


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
    )
    game = models.ForeignKey(
        Games,
        on_delete=models.CASCADE,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )
