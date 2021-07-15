import random

from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Games, GamesCategory, Image


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_games():
    products = Games.objects.all()

    return random.sample(list(products), 4)


def get_same_games(hot_product):
    same_products = Games.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)

    return same_products


def gallery(request, pk=None):
    title = 'gallery'
    basket = get_basket(request.user)
    # basket = []
    # if request.user.is_authenticated:
    #     basket = Basket.objects.filter(user=request.user)

    links_menu = GamesCategory.objects.all()
    games = Games.objects.all().order_by('price')
    if pk is not None:
        if pk == 0:
            games = Games.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(GamesCategory, pk=pk)
            games = Games.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'games': games,
            'category': category,
        }
        return render(request=request, template_name='mainapp/gallery.html', context=context)

    hot_games = get_hot_games()
    same_games = get_same_games(hot_games[0])

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_games': hot_games,
        'same_games': same_games,
        'games': games,
        'basket': basket,
    }

    return render(request=request, template_name='mainapp/gallery.html', context=context)


def game(request, pk):
    title = 'game'
    link_img = Image.objects.filter(game__pk=pk)

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'links_menu': GamesCategory.objects.all(),
        'game': get_object_or_404(Games, pk=pk),
        'link_img': link_img,
        #'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/base_game.html', context)
