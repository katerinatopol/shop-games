from django.shortcuts import render


def gallery(request):
    return render(request, 'gallery.html')


def assasin(request):
    return render(request, "assasin's_creed.html")


def ryse(request):
    return render(request, 'ryse.html')


def tomb_raider(request):
    return render(request, 'tomb_raider.html')


def warcraft(request):
    return render(request, 'warcraft.html')
