#Écrire un programme demandant un entier à un utilisateur et lui retournant sa parité. Ex.: Le nombre «4» est paire.

def parite ():

    nombre = int(input("Entrer un nombre entier : "))

    if nombre%2 == 0:
        print ("Votre nombre est pair")

    else:
        print ("votre nombre est impair")

    return None

parite()