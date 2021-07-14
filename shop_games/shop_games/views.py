from django.shortcuts import render

from basketapp.models import Basket


def index(request):
    title = 'home'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'shop_games/index.html', context=context)


def contacts(request):
    title = 'contact us'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'shop_games/contact.html', context=context)


def about(request):
    title = 'about us'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'shop_games/about.html', context=context)


def services(request):
    title = 'services'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'shop_games/services.html', context=context)


def news(request):
    title = 'news'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'shop_games/news.html', context=context)


def team(request):
    title = 'team'

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'shop_games/team.html', context=context)
