from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Games


def basket(request):
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user).order_by('game__category')
        context = {
            'basket': basket
        }
        return render(request, 'basketapp/basket.html', context)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    game = get_object_or_404(Games, pk=pk)

    basket = Basket.objects.filter(user=request.user, game=game).first()

    if not basket:
        basket = Basket(user=request.user, game=game)

    # basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))