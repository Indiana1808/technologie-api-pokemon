from fastapi import FastAPI #permet la creation des application web en utilisant le framework fast api
from fastapi.responses import HTMLResponse #inmorte la classe HTMLResponse pour retourner les reponses html
from jinja2 import Environment, FileSystemLoader #importe les classe pour génerer html  
from os.path import join, dirname #pour joindre de fichier et recuperer le nom de repertoire

import uvicorn #permet de  lancer un serveur web pour app fastapi
from pymysql import connect#connecter bdd
import json

app = FastAPI()#creer une instance en utilisant fast api 
templates = Environment(loader=FileSystemLoader(join(dirname(__file__))))


conn = connect(host='localhost', user='root', password='', db='pokemonapi') #connexion bdd
#get pour récuperer tout les pokemons
@app.get("/pokemon")
def get_pokemon():
    cursor = conn.cursor()
    cursor.execute("SELECT id_pokemon, numero_du_pokedex, nom, taille, poids, image, type_id, competence_id FROM pokemon")
    pokemon = cursor.fetchall()
    keys = [col[0] for col in cursor.description]#récupere les noms des colonnes pour utilisé comme clé de dict qui vont etre creer à partir des resultat
    pokemon = [dict(zip(keys, row)) for row in pokemon]#cree une liste de dict en utilisant les colonnes récuperer precedement 
    template = templates.get_template("pokemon.html")#charge fichier html
    rendered_template = template.render(pokemon=pokemon)#utilise contenu chargé pour génerer contenue html 
    return HTMLResponse(content=rendered_template)#retourne reponse html
#get by id
@app.get("/pokemon/{pokemon_id}")
def get_pokemon(pokemon_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE id_pokemon = %s", (pokemon_id,))
    pokemon = cursor.fetchone()
    return pokemon
@app.get("/pokemon/{nom}")
def get_pokemon(nom: str):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE nom = %s", (nom,))
    pokemon = cursor.fetchone()
    return pokemon 


#get type by id
@app.get("/type/{id_type}")
def get_type(id_type: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM types WHERE id_type = %s", (id_type,))
    type = cursor.fetchone()
    return type
#get toutes competence 
@app.get("/competence")
def get_competence():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM competence")
    competence = cursor.fetchall()
    return competence
#get toutes competence by id
@app.get("/competence/{id_competence}")
def get_competence(id_competence: int):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM competence WHERE id_competence = %s", (id_competence,))
    competence = cursor.fetchall()
    return competence
#get les types de pokemon
@app.get("/pokemons/{pokemon_id}/type")
def get_pokemon_types(pokemon_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT type.nom FROM pokemon JOIN type ON pokemon.type_id = type.id_type WHERE pokemon.id_pokemon = %s", (pokemon_id,))
    types = cursor.fetchall()
    return types


#get les competences de pokemon
@app.get("/pokemons/{pokemon_id}/competence") 
def get_pokemon_abilities(pokemon_id: int):
    cursor = conn.cursor()
    cursor.execute("SELECT competence.nom FROM pokemon JOIN competence ON pokemon.competence_id = competence.id_competence WHERE pokemon.id_pokemon = %s", (pokemon_id,))
    abilities = cursor.fetchall()
    return abilities
#post pokemon 
@app.post("/pokemon")
def create_pokemon(pokemon: dict):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon (numero_du_pokedex, nom, taille, poids, statistiques_de_base, image, type_id, competence_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (pokemon['numero_du_pokedex'], pokemon['nom'], pokemon['taille'], pokemon['poids'], pokemon['statistiques_de_base'], pokemon['image'], pokemon['type_id'], pokemon['competence_id']))
    conn.commit()
    return {"id_pokemon": cursor.lastrowid}
#post competence 
@app.post("/competence")
def create_pokemon(competence: dict):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO competence (id_competence, nom, description, puissance, precision, pp_max, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", (competence['id_competence'], competence['nom'], competence['description'], competence['puissance'], competence['precision'], competence['pp_max'], competence['type_id']))
    conn.commit()
    return {"id_competence": cursor.lastrowid}
#post type 
@app.post("/type")
def create_pokemon(type: dict):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO type (id_type, nom, typeForts, typeFaibles) VALUES (%s, %s, %s, %s)", (type['id_type'], type['nom'], type['typeForts'], type['typeFaibles']))
    conn.commit()
    return {"id_type": cursor.lastrowid}
#update pokemon by id
@app.put("/pokemon/{pokemon_id}")
def update_pokemon(pokemon_id: int, pokemon: dict):
    cursor = conn.cursor()
    cursor.execute("UPDATE pokemon SET numero_du_pokedex = %s, nom = %s, taille = %s, poids = %s, statistiques_de_base = %s, image = %s, type_id = %s, competence_id = %s WHERE id_pokemon = %s", (pokemon['numero_du_pokedex'], pokemon['nom'], pokemon['taille'], pokemon['poids'], pokemon['statistiques_de_base'], pokemon['image'], pokemon['type_id'], pokemon['competence_id'], pokemon_id))
    conn.commit()
    return {"id_pokemon": pokemon_id}
#update competence by id
@app.put("/competence/{id_competence}")
def update_competence(id_competence: int, competence: dict):
    cursor = conn.cursor()
    cursor.execute("UPDATE competence SET nom = %s, description = %s, puissance = %s, precision = %s, pp_max = %s, type_id = %s WHERE id_competence = %s", (competence['nom'], competence['description'], competence['puissance'], competence['precision'], competence['pp_max'], competence['type_id'], id_competence))
    conn.commit()
    return {"id_competence": id_competence}
# update type by id 
@app.put("/type/{id_type}")
def update_type(id_type: int, type: dict):
    cursor = conn.cursor()
    cursor.execute("UPDATE type SET nom = %s, typeForts = %s, typeFaibles = %s WHERE id_type = %s", (type['nom'], type['typeForts'], type['typeFaibles'], id_type))
    conn.commit()
    return {"id_type": id_type}
#delete pokemon by id 
@app.delete("/pokemon/{id_pokemon}")
def delete_pokemon(pokemon_id: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pokemon WHERE id_pokemon = %s", (pokemon_id,))
    conn.commit()
    return {"id_pokemon": pokemon_id}
# delete competence by id
@app.delete("/competence/{id_competence}")
def delete_competence(id_competence: int):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM competence WHERE id_competence = %s", (id_competence,))
    conn.commit()
    return {"id_competence": id_competence}

# Chargement du fichier JSON
with open('pokemon.json', 'r') as f:
    pokemon_list = json.load(f)

# Boucle sur chaque pokémon dans le fichier JSON
for pokemon in pokemon_list:
    # Récupération des données du pokémon
    numero_du_pokedex = pokemon['numero_du_pokedex']
    nom = pokemon['nom']
    taille = pokemon['taille']
    poids = pokemon['poids']
    statistiques_de_base = pokemon['statistiques_de_base']
    image = pokemon['image']
    type_id = pokemon['type_id']
    competence_id = pokemon['competence_id']

# Insertion du pokémon dans la base de données MySQL
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pokemon (numero_du_pokedex, nom, taille, poids, statistiques_de_base, image, type_id, competence_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (numero_du_pokedex, nom, taille, poids, statistiques_de_base, image, type_id, competence_id))

# Validation des changements dans la base de données
conn.commit()

if __name__ == '__main__':
   uvicorn.run(app, host="localhost", port=8000)

conn.close()
