from colorama import Fore, Back, Style, init
init(autoreset=True)
import requests
import json
base = 'http://superheroapi.com/api/2045605122134217/'
buscador = 'http://superheroapi.com/api/2045605122134217/search/'
continuar = False
heroeID = ""

def pelea (heroeID):
	heroe = requests.get(base + heroeID)
	if heroe.status_code == 200:
		esquemaHeroe = heroe.json()
		inte = int(esquemaHeroe['powerstats']['intelligence'])
		if inte >= 80:
			inte = inte * 0.2
		else:
			inte = inte
		fuer = int(esquemaHeroe['powerstats']['strength'])
		if fuer >= 50:
			fuer = fuer * 0.25
		else:
			fuer = fuer
		velo = int(esquemaHeroe['powerstats']['speed'])
		if velo >= 40:
			velo = velo * 0.15
		else:
			velo = velo
		dura = int(esquemaHeroe['powerstats']['durability'])
		if dura >= 50:
			dura = dura * 0.50
		else:
			dura = dura
		pode = int(esquemaHeroe['powerstats']['power'])
		if pode >= 105:
			pode = pode * 0.45
		else:
			pode = pode
		comb = int(esquemaHeroe['powerstats']['combat'])
		if comb >= 100:
			comb = comb * 0.35
		else:
			comb = comb
		poderTotal = inte+fuer+velo+dura+pode+comb
	return poderTotal

def menu (heroeID):
	print (Fore.GREEN + Style.BRIGHT + "Vas a buscar un superhéroes, por favor, indica un nombre:")
	heroesBuscar = input ("Nombre del héroe: ")
	print(Style.RESET_ALL)
	heroes = requests.get(buscador + heroesBuscar)
	if heroes.status_code == 200:
		esquema = heroes.json()
		print (Style.BRIGHT + "Resultados:")
		print ("El id de",Back.RED +esquema['results'][0]['name'],"es:",Back.RED +esquema['results'][0]['id'])
		#print ("El id de:",esquema['results'][1]['name'],"es:",esquema['results'][1]['id'])
		print (" ")
		heroeID = input ("¿En qué resultado quieres entrar? (Indique id): ")
		print (" ")
	return heroeID

def opciones (heroeID):
	salir = False
	if heroes.status_code == 200:
		esquemaAtrib = heroes.json()
		while salir == False:
			print (Style.BRIGHT + "Estás en el menú de la id:",Back.RED +heroeID)
			print (Fore.YELLOW + "1. Resumen de habilidades.")
			print (Fore.YELLOW + "2. Biografía.")
			print (Fore.YELLOW + "3. Apariencia")
			print (Fore.YELLOW + "4. Comics.")
			print (Fore.YELLOW + "5. Conexiones")
			print (Fore.WHITE + "6. Salir")
			seleccion = int(input ("¿Qué quieres hacer?: "))
			print (" ")
			if seleccion == 1:
				print (Style.BRIGHT + "Resumen de habilidades:")
				print (Style.DIM + Fore.RED + "Poder:",esquemaAtrib['powerstats']['power'])
				print (Style.DIM + Fore.RED + "Poder de combate:",esquemaAtrib['powerstats']['combat'])
				print (Style.DIM + Fore.RED + "Durabilidad:",esquemaAtrib['powerstats']['power'])
				print (Style.DIM + Fore.RED + "Inteligencia:",esquemaAtrib['powerstats']['power'])
				print (Style.DIM + Fore.RED + "Fuerza:",esquemaAtrib['powerstats']['power'])
				print (Style.DIM + Fore.RED + "Velocidad:",esquemaAtrib['powerstats']['power'])
				print (" ")
			if seleccion == 2:
				print (Style.BRIGHT + "Biografía:")
				print (Style.DIM + Fore.RED + "Nombre:",esquemaAtrib['biography']['full-name'])
				print (Style.DIM + Fore.RED + "Nombre de superheroe:",esquemaAtrib['name'])
				print (Style.DIM + Fore.RED + "Lugar de nacimiento:",esquemaAtrib['biography']['place-of-birth'])
				print (Style.DIM + Fore.RED + "Alter egos:",esquemaAtrib['biography']['alter-egos'])
				print (Style.DIM + Fore.RED + "Alias:")
				for x in esquemaAtrib['biography']['aliases']:
					print (x)
				print (Style.DIM + Fore.RED + "Alineación:",esquemaAtrib['biography']['alignment'])
				print (Style.DIM + Fore.RED + "Base:",esquemaAtrib['work']['base'])
				print (" ")
			if seleccion == 3:
				print (Style.BRIGHT + "Apariencia:")
				print (Style.DIM + Fore.RED + "Raza:",esquemaAtrib['appearance']['race'])
				print (Style.DIM + Fore.RED + "Género:",esquemaAtrib['appearance']['gender'])
				print (Style.DIM + Fore.RED + "Color de ojos:",esquemaAtrib['appearance']['eye-color'])
				print (Style.DIM + Fore.RED + "Color del pelo:",esquemaAtrib['appearance']['hair-color'])
				print (Style.DIM + Fore.RED + "Peso:",esquemaAtrib['appearance']['weight'][1])
				print (Style.DIM + Fore.RED + "Altura:",esquemaAtrib['appearance']['height'][1])
				print (" ")
			if seleccion == 4:
				print (Style.BRIGHT + "Comics:")
				print (Style.DIM + Fore.RED + "Primera aparición:",esquemaAtrib['biography']['first-appearance'])
				print (Style.DIM + Fore.RED + "Editorial:",esquemaAtrib['biography']['publisher'])
				print (Style.DIM + Fore.RED + "Imágen",esquemaAtrib['image']['url'])
				print (" ")
			if seleccion == 5:
				print (Style.BRIGHT + "Conexiones:")
				print (Style.DIM + Fore.RED + "Familia:",esquemaAtrib['connections']['relatives'])
				print (Style.DIM + Fore.RED + "Grupos:",esquemaAtrib['connections']['group-affiliation'])
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

poderTotal = 0
heroeID = ""

combate = input (Style.BRIGHT + "¿Quieres echar un combate?: ")
print (" ")
if combate == "S" or combate == "s":
	print (Style.BRIGHT + Fore.GREEN + "Plantel:")
	print ("□ Iron man - ID 346")
	print ("□ Spiderman - ID 620")
	print ("□ Capitán América - ID 149")
	print ("□ Batman - ID 70")
	print ("□ Superman - ID 644")
	print ("□ Joker - ID 370")
	print (" ")
	heroeID = input ("Dime una ID: ")
	poderTotal1 = pelea (heroeID)
	print (" ")
	heroeID = input ("Dime una ID: ")
	poderTotal2 = pelea (heroeID)
	print (" ")
	if poderTotal1 > poderTotal2:
		print (Back.YELLOW + "El primer jugador gana.")
	else:
		print (Back.YELLOW + "El segundo jugador gana.")
else:
	print ("Adiós")