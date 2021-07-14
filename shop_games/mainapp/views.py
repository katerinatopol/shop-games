from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Games, GamesCategory, Image


def gallery(request, pk=None):
    title = 'gallery'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    games = Games.objects.all()
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

       # hot_product = get_hot_product()
       # same_products = Product.objects.all()[3:5]# get_same_products(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        #'hot_product': hot_product,
        #'same_products': same_products,
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
