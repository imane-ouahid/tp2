import csv

def charger_pokemons_csv(fichier):
    pokemons = {}
    with open (fichier, newline="") as csvfile:
        reader = csv.reader(csvfile)

        for row in  reader:
            nom=row[0]
            status=list((int, row[1:]))
            pokemons[nom]= status
    return pokemons

pkmn = charger_pokemons_csv("pokemons.csv")
for nom, stats in pkmn.items():
    print(f"{nom}: {stats}")

pkmn = charger_pokemons_csv("pokemons.csv")
print(isinstance(pkmn, dict))
print(isinstance(pkmn["Pikachu"], list))
print(isinstance(pkmn["Pikachu"][0], int))
