from matplotlib.pyplot import *
import csvReader as csv
from math import *


fichierPokemon = csv.importCSV("pokemons.csv", separateur=';')
# print(fichierPokemon)
fichierPokemonFiltrer = csv.filtrerColonne(fichierPokemon, ['nom','vie','attaque','defense','type1'])

for i in range(len(fichierPokemon)):
	fichierPokemonFiltrer[i]['vie']=int(fichierPokemonFiltrer[i]['vie'])
	fichierPokemonFiltrer[i]['attaque']=int(fichierPokemonFiltrer[i]['attaque'])
	fichierPokemonFiltrer[i]['defense']=int(fichierPokemonFiltrer[i]['defense'])


print(fichierPokemonFiltrer[0])  # affiche {'nom': 'Rattata', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal'}
pokemon1 = csv.filtrerLigne(fichierPokemonFiltrer, 'type1', 'Feu')
pokemon2 = csv.filtrerLigne(fichierPokemonFiltrer, 'type1', 'Psy')

fig = figure()
ax = fig.add_subplot(111)
X = [pikapika['vie'] for pikapika in pokemon1]
Y = [pikapika['attaque'] for pikapika in pokemon1]
Z = [pikapika['defense'] for pikapika in pokemon1]
ax.plot(X,Y,'db',label='Feu')

X = [pikapika['vie'] for pikapika in pokemon2]
Y = [pikapika['attaque'] for pikapika in pokemon2]
Z = [pikapika['defense'] for pikapika in pokemon2]
ax.plot(X,Y,'or',label='Psy')
X = 65
Y = 40
ax.plot(X,Y,'sg',markersize=10,label='Qui suis-je?')
ax.set_xlabel('Points de vie')
ax.set_ylabel("Points d'attaque")
ax.legend()
majorXticks = range(20, 121, 10)
majorYticks = range(0, 201, 10)
ax.set_xticks(majorXticks)
ax.set_yticks(majorYticks)
ax.grid()
ax.set(xlim=(20, 120), ylim=(0, 200))
show()

print(fichierPokemonFiltrer[0])  # affiche {'nom': 'Rattata', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal'}
# fichierPokemonFiltrer  est un tableau de dictionnaires
#[
# {'nom': 'Rattata', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal'}, 
# {'nom': 'Grosbil', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal'}
#]

def kNN(table, cible, k):
	''' 
	table : liste de Pokemon sous forme de dictionnaire dont on va extraire deux caractéristiques (vie, force)
	cible : caractéristique du Pokémon donné (vie, force)
	k     : nombre de plus proches voisins
	'''

	def distance(pokemon, cible):
		# distance entre un pokemon et une cible **(vie, attaque)**
		# pokemon est de la forme : pokemon = {'nom': 'Rattata', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal'}
		# cible est de la forme : cible = (vie, attaque)
		vie = pokemon['vie']
		attaque = pokemon['attaque']
		# d = 
		return d 
	
	# on ajout une nouvelle colonne "distance" à la base de données des pokémons 
	for num, pokemon in enumerate(table):
		table[num]["distance"] = distance(pokemon, cible) # merci enumerate !
		#  table[num]["distance"] = distance(table[num], cible) 

	#print(table[0:3])

	# On trie de la table selon la colonne "distance"
	'''
	[
	 {'nom': 'Rattata', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal', 'distance': 85.47514258543241}, 
	 {'nom': 'Rattata', 'vie': 30, 'attaque': 56, 'defense': 35, 'type1': 'Normal', 'distance': 85.47514258543241}, 
	 {'nom': 'Rattatac', 'vie': 55, 'attaque': 81, 'defense': 60, 'type1': 'Normal', 'distance': 62.0966987850401}
	]
	'''

	tableTriee = []



	# [{'nom': 'Symbios', 'vie': 110, 'attaque': 65, 'defense': 75, 'type1': 'Psy', 'distance': 5.0}, 
	# {'nom': 'Cresselia', 'vie': 120, 'attaque': 70, 'defense': 120, 'type1': 'Psy', 'distance': 7.0710678118654755}, 
	# {'nom': 'Mushana', 'vie': 116, 'attaque': 55, 'defense': 85, 'type1': 'Psy', 'distance': 10.04987562112089}]

	# on regarde les k premiers voisins
	prochesVoisins = []
	for i in range(k):
		prochesVoisins.append(tableTriee[i]['type1'])
	
	#print(prochesVoisins)
#    ['Psy', 'Psy', 'Normal', 'Normal', 'Normal', 'Psy', 'Psy']
	typeFinal = ''
		
	return typeFinal
 

 
types = kNN(fichierPokemonFiltrer, (105,65), 5)
