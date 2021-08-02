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

# Pokémon 1
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[0])

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon["name"])
moves = pokemon["moves"]

f = open("pokemon.txt", "w+")
f.write(pokemon["name"] + " ")
for move in moves:
    f.write("""
    """ + move["move"]["name"])
f.close()

# Pokémon 2
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[1])

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon["name"])
moves = pokemon["moves"]

f = open("pokemon.txt", "a+")
f.write("""
""" + pokemon["name"])
for move in moves:
    f.write("""
    """ + move["move"]["name"])
f.close()

# Pokémon 3
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[2])

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon["name"])
moves = pokemon["moves"]

f = open("pokemon.txt", "a+")
f.write("""
""" + pokemon["name"])
for move in moves:
    f.write("""
    """ + move["move"]["name"])
f.close()

# Pokémon 4
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[3])

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon["name"])
moves = pokemon["moves"]

f = open("pokemon.txt", "a+")
f.write("""
""" + pokemon["name"])
for move in moves:
    f.write("""
    """ + move["move"]["name"])
f.close()

# Pokémon 5
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[4])

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon["name"])
moves = pokemon["moves"]

f = open("pokemon.txt", "a+")
f.write("""
""" + pokemon["name"])
for move in moves:
    f.write("""
    """ + move["move"]["name"])
f.close()

# Pokémon 6
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_list[5])

response = requests.get(url)
print(response)

pokemon = response.json()
print(pokemon["name"])
moves = pokemon["moves"]

f = open("pokemon.txt", "a+")
f.write("""
""" + pokemon["name"])
for move in moves:
    f.write("""
    """ + move["move"]["name"])
f.close()

print("Gotta catch 'em all!")