from django.shortcuts import render
from .models import Photo, Annonsment, Advertize


def all_content_view(request):
    photos = Photo.objects.all()
    advertizes = Advertize.objects.all()
    anonsments = Annonsment.objects.all()

    context = {
        'photos': photos,
        'advertizes': advertizes,
        'anonsments': anonsments,
    }
    return render(request, 'gallery/photo_list.html', context)