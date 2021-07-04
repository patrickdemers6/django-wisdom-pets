from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404

from .models import Pet


def home(request: HttpRequest) -> HttpResponse:
    pets: list[Pet] = Pet.objects.all()

    return render(request, 'home.html', {
        'pets': pets
    })


def pet_detail(request: HttpRequest, pet_id: int) -> HttpResponse:
    try:
        pet = Pet.objects.get(id=pet_id)
    except Pet.DoesNotExist:
        raise Http404('Pet not found')

    return render(request, 'pet_detail.html', {
        'pet': pet
    })
