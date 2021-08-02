"""
Code First Girls Homework 5.3
In this session you used the Pokemon API to retrieve a single Pokemon.
I want a program that can retrieve multiple Pokemon and save their names and moves to a file.

Use a list to store about 6 Pokemon IDs. Then in a for loop
call the API to retrieve the data for each Pokemon.
Save their names and moves into a file called 'pokemon.txt'
"""
import requests

pokemon_list = [83, 94, 79, 52, 151, 289]

def pokemon_moves(pokemon_id, f):
    global url, response, pokemon, moves, move
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_id)
    response = requests.get(url)
    pokemon = response.json()
    print(pokemon["name"].title())
    moves = pokemon["moves"]
    f.write(pokemon["name"].title() + "\n")
    for move in moves:
        f.write("\t" + move["move"]["name"].title() + "\n")

f = open("pokemon.txt", "w+")
f.write("Check out my smooth moves! \n")

for pokemon in pokemon_list:
    pokemon_moves(pokemon, f)

f.close()

print("Gotta catch 'em all!")
