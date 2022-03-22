#Créer un dictionnaire possédant les cours que vous suivez cette session et leur enseignant respectif. Par exemple:
# Keven Presseau-St-Laurent - Concepts de programmation 1 Ensuite, afficher un menu à la console présentant les 5 cours 
# et offrant à l'utilisateur d'en sélectionner 1. Lorsque l'utilisateur à fait sa sélection, afficher le nom de l'enseignant et le nom du cours à l'écran.

def dictionnaire():

    dict = {"Keven Presseau-St-Laurent" : "Concepts de programmation 1", "Emma Senez Parent": "Logique mathématique", "Jean-Pierre Fiset": "système d'exploitation"}

    print(dict)

    choix = int(input("Choisir un cours (1, 2 ou 3): "))

    if choix == 1:
        print(f"Keven Presseau-st-laurent", dict["Keven Presseau-St-Laurent"])

    elif choix == 2:
        print(f"Emma Senez Parent", dict["Emma Senez Parent"])

    else:
        print(f"Jean-Pierre Fiset", dict["Jean-Pierre Fiset"])

    return choix


#dictionnaire()


#En se basant sur l'exercice 3, créer un fichier bdd.txt fonctionnant comme une base de données
# et remplir le dictionnaire à partir de ce fichier. Pour vous faciliter la tâche, vous pouvez écrire
# les informations de la manière suivante: Nom de cours 1, Nom de prof 1, Nom de cours 2

def fichier():

    mon_fichier = open("bdd.txt", "r", encoding="utf8")
    contenu = mon_fichier.readlines()
    mon_fichier.close()
    dico = {contenu[0] : contenu[1], contenu[2] : contenu[3], contenu[4] : contenu[5]}

    return dico

#dic1 = fichier()


#En se basant sur l'exercice 4, modifier le menu utilisateur en y ajoutant une option lui permettant de faire une recherche d'enseignant.
#Vérifier si l'enseignant entré par l'utilisateur est présent
#dans votre liste de cours et indiquer le résultat à la console.

def exercice5(dico_entrant):
     
    enseignant = (input("Entrer le nom de votre enseignant: "))    

    enseignant1 = enseignant + "\n"

    if enseignant1 in dico_entrant:
        print("Votre enseignant est dans la liste : ")

    else:
        print("pas dans la liste")

    return None

#exercice5(dic1)


#Offrir à l'utilisateur une nouvelle option au menu lui permettant d'ajouter un cours et un nom d'enseignant
# à la base de données de l'exercice 4. Une fois les données utilisateurs entrées,
# ajouter les informations à la fin du document bdd.txt


def exercice6():

    ajout_en = input("Ajouter votre enseignant: ")
    ajout_cours = input("Ajouter le nom du cours ")

    mon_fichier = open("bdd.txt", "a", encoding ="utf8")
    mon_fichier.write(f"\n{ajout_en}\n{ajout_cours}")
    mon_fichier.close()


exercice6()



    


        
  





    