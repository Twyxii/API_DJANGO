from django.shortcuts import render

# Create your views here.

# views.py

from django.http import JsonResponse
from .models import *

def get_item(request, item_id):
    try:
        item = items.objects.get(id=item_id)
        data = {
            'id': item.id,
            'identifier': item.identifier,
            'category_id': item.category_id,
            'cost': item.cost,
            'fling_power': item.fling_power,
            'fling_effect_id': item.fling_effect_id
        }
        return JsonResponse(data)
    except items.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

def get_move(request, move_id):
    try:
        move = moves.objects.get(id=move_id)
        data = {   
            'id': move.id,
            'identifier': move.identifier,
            'generation_id': move.generation_id,
            'type_id': move.type_id,
            'power': move.power,
            'pp': move.pp,
            'accuracy': move.accuracy,
            'priority': move.priority,
            'target_id': move.target_id,
            'damage_class_id': move.damage_class_id,
            'effect_id': move.effect_id,
            'effect_chance': move.effect_chance,
            'contest_type_id': move.contest_type_id,
            'contest_effect_id': move.contest_effect_id,
            'super_contest_effect_id': move.super_contest_effect_id      
        }
        return JsonResponse(data)
    except moves.DoesNotExist:
        return JsonResponse({'error': 'Move not found'}, status=404)

def get_pokemon(request, pokemon_id):
    try:
        pokemon = pokemon.objects.get(id=pokemon_id)
        data = {
            'id': pokemon.id,
            'identifier': pokemon.identifier,
            'species_id': pokemon.species_id,
            'height': pokemon.height,
            'weight': pokemon.weight,
            'base_experience': pokemon.base_experience,
            'order': pokemon.order,
            'is_default': pokemon.is_default
        }
        return JsonResponse(data)
    except pokemon.DoesNotExist:
        return JsonResponse({'error': 'Pokemon not found'}, status=404)

def get_egg_group(request,egg_group_id):
    try:
        egg_groups = egg_groups.objects.get(id=egg_group_id)
        data = {
            'id': egg_groups.id,
            'identifier':egg_groups.identifier
        }
        return
    except egg_groups.DoesNotExist:
        return JsonResponse({'error': 'egg group not found'}, status=404)

def get_types(request, type_id):
    try:
        type_obj = types.objects.get(id=type_id)
        data = {
            'id': type_obj.id,
            'identifier': type_obj.identifier,
            'generation_id': type_obj.generation_id,
            'damage_class_id': type_obj.damage_class_id
        }
        return JsonResponse(data)
    except types.DoesNotExist:
        return JsonResponse({'error': 'Type not found'}, status=404)

def get_stats(request, stat_id):
    try:
        stat = stats.objects.get(id=stat_id)
        data = {
            'id': stat.id,
            'damage_class_id': stat.damage_class_id,
            'identifier': stat.identifier,
            'is_battle_only': stat.is_battle_only,
            'game_index': stat.game_index
        }
        return JsonResponse(data)
    except stats.DoesNotExist:
        return JsonResponse({'error': 'Stat not found'}, status=404)

def get_pokemon_types(request, pokemon_type_id):
    try:
        pokemon_type = pokemon_types.objects.get(id=pokemon_type_id)
        data = {
            'id': pokemon_type.id,
            'pokemon_id': pokemon_type.pokemon_id,
            'type_id': pokemon_type.type_id,
            'slot': pokemon_type.slot
        }
        return JsonResponse(data)
    except pokemon_types.DoesNotExist:
        return JsonResponse({'error': 'Pokemon type not found'}, status=404)

def get_pokemon_stat(request, pokemon_stat_id):

    try:
        pokemon_stat = pokemon_stats.objects.get(id=pokemon_stat_id)
        data = {
            'id': pokemon_stat.id,
            'pokemon_id': pokemon_stat.pokemon_id,
            'stat_id': pokemon_stat.stat_id,
            'base_stat': pokemon_stat.base_stat,
            'effort': pokemon_stat.effort
        }
        return JsonResponse(data)
    except pokemon_stats.DoesNotExist:
        return JsonResponse({'error': 'Pokemon stat not found'}, status=404)
    
def get_location(request, location_id):
    try:
        location = Location.objects.get(id=location_id)
        data = {
            'id': location.id,
            'region_id': location.region_id,
            'identifier': location.identifier
        }
        return JsonResponse(data)
    except Location.DoesNotExist:
        return JsonResponse({'error': 'Location not found'}, status=404)

def get_pokemon_move(request, pokemon_move_id):
    try:
        pokemon_move = pokemon_moves.objects.get(id=pokemon_move_id)
        data = {
            'id': pokemon_move.id,
            'pokemon_id': pokemon_move.pokemon_id,
            'version_group_id': pokemon_move.version_group_id,
            'move_id': pokemon_move.move_id,
            'pokemon_move_method_id': pokemon_move.pokemon_move_method_id,
            'level': pokemon_move.level,
            'order': pokemon_move.order
        }
        return JsonResponse(data)
    except pokemon_moves.DoesNotExist:
        return JsonResponse({'error': 'Pokemon move not found'}, status=404)

def get_pokemon_form_generation(request, pokemon_form_generation_id):
    try:
        pokemon_form_generation = pokemon_form_generations.objects.get(id=pokemon_form_generation_id)
        data = {
            'pokemon_form_id': pokemon_form_generation.pokemon_form_id,
            'generation_id': pokemon_form_generation.generation_id,
            'game_index': pokemon_form_generation.game_index
        }
        return JsonResponse(data)
    except pokemon_form_generations.DoesNotExist:
        return JsonResponse({'error': 'Pokemon form generation not found'}, status=404)