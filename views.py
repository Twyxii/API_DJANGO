from django.shortcuts import render

# Create your views here.

# views.py

from django.http import JsonResponse
from .models import Item, Move, Pokemon

def item_detail(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        data = {
            'name': item.name,
            'description': item.description
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

def move_detail(request, move_id):
    try:
        move = Move.objects.get(id=move_id)
        data = {
            'name': move.name,
            'power': move.power
        }
        return JsonResponse(data)
    except Move.DoesNotExist:
        return JsonResponse({'error': 'Move not found'}, status=404)

def pokemon_detail(request, pokemon_id):
    try:
        pokemon = Pokemon.objects.get(id=pokemon_id)
        data = {
            'name': pokemon.name,
            'type': pokemon.type,
            'level': pokemon.level
        }
        return JsonResponse(data)
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

