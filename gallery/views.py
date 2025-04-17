from django.shortcuts import render
from .models import Promo, Photo, Annonsment, Advertize, Contact


def all_content_view(request):
    promos = Promo.objects.all()
    photos = Photo.objects.all()
    advertizes = Advertize.objects.all()
    anonsments = Annonsment.objects.all()

    context = {
        'promos': promos,
        'photos': photos,
        'advertizes': advertizes,
        'anonsments': anonsments,
    }
    return render(request, 'gallery/photo_list.html', context)

