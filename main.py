import json
import os
# import du module mysql.connector
from mysql.connector import connect, DatabaseError, InterfaceError
from django.urls import path


# views.py
from . import views
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Item, Move, Pokemon
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework_jwt.settings import api_settings

USER = "root1"
PWD = ""
HOST = "localhost"
DATABASE = "pokedex"


# connexion à une base MySql [dbpersonnes]
# l'identité de l'utilisateur est (admpersonnes,nobody)

# c'est parti
connexion = None
try:
    print("Connexion au SGBD MySQL en cours...")
    # connexion
    connexion = connect(host=HOST, user=USER, password=PWD, database=DATABASE)
    # suivi
    print(
        f"Connexion MySQL réussie à la base database={DATABASE}, host={HOST} sous l'identité user={USER}, passwd={PWD}")
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
finally:
    # on ferme la connexion si elle a été ouverte
    if connexion:
        connexion.close()





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
]


@api_view(['GET'])
def get_item(request,item_id):
    item = Item.objects.get(id=item_id)
    data = { 'id': item.id, 'name': item.name}
    return JsonResponse, 201

