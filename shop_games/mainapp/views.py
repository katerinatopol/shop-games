from django.shortcuts import render


def gallery(request):
    return render(request, 'mainapp/gallery.html')


def assasin(request):
    return render(request, "mainapp/assasin's_creed.html")


def ryse(request):
    return render(request, 'mainapp/ryse.html')


def tomb_raider(request):
    return render(request, 'mainapp/tomb_raider.html')


def warcraft(request):
    return render(request, 'mainapp/warcraft.html')
