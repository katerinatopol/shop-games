from django.shortcuts import render


def gallery(request):
    title = 'gallery'
    context = {
        'title': title,
    }
    return render(request, 'mainapp/gallery.html', context=context)


def assasin(request):
    title = "assasin's creed"
    links_img = [
        "/static/mainapp/img/assassin/assassin_1.jpg",
        "/static/mainapp/img/assassin/assassin_2.jpg",
        "/static/mainapp/img/assassin/assassin_3.jpg",
        "/static/mainapp/img/assassin/assassin_4.jpg"
    ]
    context = {
        'title': title,
        'links_img': links_img,
    }
    return render(request, "mainapp/assasin's_creed.html", context=context)


def ryse(request):
    title = 'ryse: son of rome'
    links_img = [
        "/static/mainapp/img/ryse/ryse_1.jpg",
        "/static/mainapp/img/ryse/ryse_2.jpg",
        "/static/mainapp/img/ryse/ryse_3.jpg",
        "/static/mainapp/img/ryse/ryse_4.jpg",
    ]
    context = {
        'title': title,
        'links_img': links_img,
    }
    return render(request, 'mainapp/ryse.html', context=context)


def tomb_raider(request):
    title = 'tomb raider'
    links_img = [
        "/static/mainapp/img/tomb_raider/tr_1.jpg",
        "/static/mainapp/img/tomb_raider/tr_2.jpg",
        "/static/mainapp/img/tomb_raider/tr_3.jpg",
        "/static/mainapp/img/tomb_raider/tr_4.jpg",
    ]
    context = {
        'title': title,
        'links_img': links_img,
    }
    return render(request, 'mainapp/tomb_raider.html', context=context)


def warcraft(request):
    title = 'world of warcraft'
    links_img = [
        "/static/mainapp/img/world_of_warcraft/wow_1.jpg",
        "/static/mainapp/img/world_of_warcraft/wow_2.jpg",
        "/static/mainapp/img/world_of_warcraft/wow_3.jpg",
        "/static/mainapp/img/world_of_warcraft/wow_4.jpg",
    ]
    context = {
        'title': title,
        'links_img': links_img,
    }
    return render(request, 'mainapp/warcraft.html', context=context)
