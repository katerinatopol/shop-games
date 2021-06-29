from django.shortcuts import render


def index(request):
    title = 'home'
    context = {
        'title': title,
    }
    return render(request, 'shop_games/index.html', context=context)


def contacts(request):
    title = 'contact us'
    context = {
        'title': title,
    }
    return render(request, 'shop_games/contact.html', context=context)


def about(request):
    title = 'about us'
    context = {
        'title': title,
    }
    return render(request, 'shop_games/about.html', context=context)


def services(request):
    title = 'services'
    context = {
        'title': title,
    }
    return render(request, 'shop_games/services.html', context=context)


def news(request):
    title = 'news'
    context = {
        'title': title,
    }
    return render(request, 'shop_games/news.html', context=context)


def team(request):
    title = 'team'
    context = {
        'title': title,
    }
    return render(request, 'shop_games/team.html', context=context)
