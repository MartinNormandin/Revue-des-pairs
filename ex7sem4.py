#Écrire un programme demandant à l'utilisateur de rentrer un nombre entre 1 et 20, vérifier si ce dernier est bel et bien entre 1 et 20 
# et indiquez-lui si son nombre est un nombre premier (ayant aucun autre facteur entier que 1 et lui-même)

def nombre_premier():

    nombre = int(input("Veuillez entrer un nombre entre 1 et 20: "))

    if nombre < 1 or nombre > 20:
        print ("Nombre invalide, essayer de nouveau: ")

    elif nombre == 2 or nombre == 3 or nombre == 5 or nombre == 7 or nombre == 11 or nombre == 13 or nombre == 17 or nombre == 19:
        print ("Votre nombre est un nombre premier")

    else:
        print ("Votre nombre n'est pas un nombre premier")

    return None


nombre_premier()