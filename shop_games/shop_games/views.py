from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contacts(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def news(request):
    return render(request, 'news.html')


def team(request):
    return render(request, 'team.html')
