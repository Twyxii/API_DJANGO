import json
import os
import django

from django.conf import settings
# import du module mysql.connector

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API-DJANGO.settings')
django.setup()

from django.contrib.auth.models import User
from django.urls import path


# views.py
import views
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework_jwt.settings import api_settings






urlpatterns = [
    path('api/items/<int:item_id>/', views.get_item, name='get_item'),
    path('api/moves/<int:move_id>/', views.get_move, name='get_move'),
    path('api/pokemon/<int:pk>/', views.get_pokemon_by_id, name='get_pokemon_by_id'),
    path('api/pokemon/<str:name>/', views.get_pokemon_by_name, name='get_pokemon_by_name'),
    path('api/pokemon/types/<str:pokemon_type>/', views.get_pokemon_by_type, name='get_pokemon_by_type'),
    path('api/connexion/', views.connect_user, name='connect_user'),
    path('api/register/', views.register_user, name='register_user'),
    path('api/mesPokemons/', views.get_user_pokemons, name='get_user_pokemons'),
    path('api/role/', views.get_user_role, name='get_user_role'),
    path('api/admin/users/', views.get_admin_users, name='get_admin_users'),

    # Ajout des nouveaux endpoints
    path('api/locations/<int:location_id>/', views.get_location, name='get_location'),
    path('api/pokemon_moves/<int:pokemon_move_id>/', views.get_pokemon_move, name='get_pokemon_move'),
    path('api/pokemon_form_generations/<int:pokemon_form_generation_id>/', views.get_pokemon_form_generation, name='get_pokemon_form_generation'),
]



@api_view(['GET'])
def get_item(request,item_id):
    item = items.objects.get(id=item_id)
    data = { 'id': item.id, 'name': item.name}
    return JsonResponse, 201

