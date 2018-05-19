import hashlib
import requests
import json
base = 'http://superheroapi.com/api/2045605122134217/'
buscador = 'http://superheroapi.com/api/2045605122134217/search/'
continuar = False
heroeID = ""

def menu (heroeID):
	print ("Vas a buscar un superhéroes, por favor, indica un nombre ")
	heroesBuscar = input ("Nombre del héroe: ")
	heroes = requests.get(buscador + heroesBuscar)
	if heroes.status_code == 200:
		esquema = heroes.json()
		print ("Resultados: ")
		print ("El id de:",esquema['results'][0]['name'],"es:",esquema['results'][0]['id'])
		print ("El id de:",esquema['results'][1]['name'],"es:",esquema['results'][1]['id'])
		print (" ")
		heroeID = input ("¿En qué resultado quieres entrar? (Indique id): ")
	return heroeID
def opciones (heroeID):
	salir = False
	if heroes.status_code == 200:
		esquemaAtrib = heroes.json()
		while salir == False:
			print ("Estás en el menú de la id:",heroeID)
			print ("1. Resumen de habilidades.")
			print ("2. Biografía.")
			print ("3. Apariencia")
			print ("4. Comics.")
			print ("5. Conexiones")
			print ("6. Salir")
			seleccion = int(input ("¿Qué quieres hacer?:"))
			print (" ")
			if seleccion == 1:
				print ("Resumen de habilidades:")
				print ("Poder:",esquemaAtrib['powerstats']['power'])
				print ("Poder de combate:",esquemaAtrib['powerstats']['combat'])
				print ("Durabilidad:",esquemaAtrib['powerstats']['power'])
				print ("Inteligencia:",esquemaAtrib['powerstats']['power'])
				print ("Fuerza:",esquemaAtrib['powerstats']['power'])
				print ("Velocidad:",esquemaAtrib['powerstats']['power'])
				print (" ")
			if seleccion == 2:
				print ("Biografía:")
				print ("Nombre:",esquemaAtrib['biography']['full-name'])
				print ("Nombre de superheroe:",esquemaAtrib['name'])
				print ("Lugar de nacimiento:",esquemaAtrib['biography']['place-of-birth'])
				print ("Alter egos:",esquemaAtrib['biography']['alter-egos'])
				print ("Alias:")
				for x in esquemaAtrib['biography']['aliases']:
					print (x)
				print ("Alineación:",esquemaAtrib['biography']['alignment'])
				print ("Base:",esquemaAtrib['work']['base'])
				print (" ")
			if seleccion == 3:
				print ("Apariencia:")
				print ("Raza:",esquemaAtrib['appearance']['race'])
				print ("Género:",esquemaAtrib['appearance']['gender'])
				print ("Color de ojos:",esquemaAtrib['appearance']['eye-color'])
				print ("Color del pelo:",esquemaAtrib['appearance']['hair-color'])
				print ("Peso:",esquemaAtrib['appearance']['weight'][1])
				print ("Altura:",esquemaAtrib['appearance']['height'][1])
				print (" ")
			if seleccion == 4:
				print ("Comics:")
				print ("Primera aparición:",esquemaAtrib['biography']['first-appearance'])
				print ("Editorial:",esquemaAtrib['biography']['publisher'])
				print ("Imágen",esquemaAtrib['image']['url'])
				print (" ")
			if seleccion == 5:
				print ("Conexiones:")
				print ("Familia:",esquemaAtrib['connections']['relatives'])
				print ("Grupos:",esquemaAtrib['connections']['group-affiliation'])
				print (" ")
			if seleccion == 6:
				salir = True
while continuar == False:
	heroeID = menu (heroeID)
	heroes = requests.get(base + heroeID)
	opciones(heroeID)
	seguir = input ("¿Quieres mostar más? (S/N): ")
	if seguir == "S" or seguir == "s":
		continuar = False
	elif seguir == "N" or seguir == "n":
		continuar = True
	else:
		print ("Escribe S o N.")
