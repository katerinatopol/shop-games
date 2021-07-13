from django.shortcuts import render, get_object_or_404
from mainapp.models import Games, GamesCategory


def gallery(request, pk=None):
    title = 'gallery'
    # basket = get_basket(request.user)
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
        #'basket': basket,
    }

    return render(request=request, template_name='mainapp/gallery.html', context=context)


def game(request, pk):
    title = 'game'

    context = {
        'title': title,
        'links_menu': GamesCategory.objects.all(),
        'game': get_object_or_404(Games, pk=pk),
        #'basket': get_basket(request.user),
    }

    return render(request, 'mainapp/base_game.html', context)
#
# def assasin(request):
#     title = "assasin's creed"
#     links_img = [
#         "/static/mainapp/img/assassin/assassin_1.jpg",
#         "/static/mainapp/img/assassin/assassin_2.jpg",
#         "/static/mainapp/img/assassin/assassin_3.jpg",
#         "/static/mainapp/img/assassin/assassin_4.jpg"
#     ]
#     context = {
#         'title': title,
#         'links_img': links_img,
#     }
#     return render(request, "mainapp/assasin's_creed.html", context=context)
#
#
# def ryse(request):
#     title = 'ryse: son of rome'
#     links_img = [
#         "/static/mainapp/img/ryse/ryse_1.jpg",
#         "/static/mainapp/img/ryse/ryse_2.jpg",
#         "/static/mainapp/img/ryse/ryse_3.jpg",
#         "/static/mainapp/img/ryse/ryse_4.jpg",
#     ]
#     context = {
#         'title': title,
#         'links_img': links_img,
#     }
#     return render(request, 'mainapp/ryse.html', context=context)
#
#
# def tomb_raider(request):
#     title = 'tomb raider'
#     links_img = [
#         "/static/mainapp/img/tomb_raider/tr_1.jpg",
#         "/static/mainapp/img/tomb_raider/tr_2.jpg",
#         "/static/mainapp/img/tomb_raider/tr_3.jpg",
#         "/static/mainapp/img/tomb_raider/tr_4.jpg",
#     ]
#     context = {
#         'title': title,
#         'links_img': links_img,
#     }
#     return render(request, 'mainapp/tomb_raider.html', context=context)
#
#
# def warcraft(request):
#     title = 'world of warcraft'
#     links_img = [
#         "/static/mainapp/img/world_of_warcraft/wow_1.jpg",
#         "/static/mainapp/img/world_of_warcraft/wow_2.jpg",
#         "/static/mainapp/img/world_of_warcraft/wow_3.jpg",
#         "/static/mainapp/img/world_of_warcraft/wow_4.jpg",
#     ]
#     context = {
#         'title': title,
#         'links_img': links_img,
#     }
#     return render(request, 'mainapp/warcraft.html', context=context)
