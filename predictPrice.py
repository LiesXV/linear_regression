def __main__():
	try:
		with open('thetas.txt', 'r') as f:
			theta0 = float(f.readline().strip())
			theta1 = float(f.readline().strip())
		print("Modèle chargé avec succès !")
	except FileNotFoundError:
		print("Fichier thetas.txt non trouvé")
		exit()
	except ValueError:
		print("Erreur dans le fichier thetas.txt.")
		exit()

	while True:
			try:
				user_input = input("\nEntrez le kilométrage de la voiture (ou 'q' pour quitter) : ").strip()
				
				if user_input.lower() == 'q':
					print("Au revoir !")
					break
					
				mileage = float(user_input)
				
				if mileage < 0:
					print("Le kilométrage ne peut pas être négatif. Réessayez.")
					continue
					
				estimatedPrice = theta0 + theta1 * mileage
				if estimatedPrice > 0:
					print(f"Le prix de votre voiture est estimé à environ : {estimatedPrice:.0f} €")
				else:
					print("Votre voiture ne vaut plus rien !")
				
			except ValueError:
				print("Veuillez entrer un nombre valide (ex: 100000) ou 'q' pour quitter.")

if __name__ == "__main__":
	__main__()