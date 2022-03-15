#Écrire un programme demandant un entier à un utilisateur et lui retournant sa parité. Ex.: Le nombre «4» est paire.
# pas de raison d'avoir un espace entre parite, ()
def parite():

    nombre = int(input("Entrer un nombre entier : "))
    # espace recommandé entre nombre,%,2
    if nombre % 2 == 0:
        print ("Votre nombre est pair")

    else:
        print ("votre nombre est impair")
    # pas obligé de mettre None si rien est retourné
    
# 2 lignes vides entre le bloc des fonctions et le bloc d'instructions
parite()