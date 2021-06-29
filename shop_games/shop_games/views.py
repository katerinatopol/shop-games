from django.shortcuts import render


def index(request):
    return render(request, 'shop_games/index.html')


def contacts(request):
    return render(request, 'shop_games/contact.html')


def about(request):
    return render(request, 'shop_games/about.html')


def services(request):
    return render(request, 'shop_games/services.html')


def news(request):
    return render(request, 'shop_games/news.html')


def team(request):
    return render(request, 'shop_games/team.html')
