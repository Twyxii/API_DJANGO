import json
import os
from flask import Flask, jsonify, request
# import du module mysql.connector
from mysql.connector import connect, DatabaseError, InterfaceError


app = Flask(__name__)

USER = "root1"
PWD = ""
HOST = "localhost"
DATABASE = "cours1"


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


user = [ { 'userID': 1, 'username': 'Ashley', 'email' : 'toto@tonpere.com', 'password' : 'papa', 'create_time' : 2022-2-25 }]


@app.route('/user', methods=['GET'])
def get_user():
    return jsonify(user), 201

@app.route('/user', methods=['DELETE'])
def delete_user():
    
    return jsonify("tutu!!!!"), 201

if __name__ == "__main__":
    app.run(debug=True)
