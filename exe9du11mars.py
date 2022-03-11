#Créer une calculatrice permettant de calculer combien couteraient en 2021, un article acheté en 1970. Utilisez le IPC moyenne annuelle de
# ces années respectives.
# Les données sont disponibles ici: https://www150.statcan.gc.ca/n1/pub/71-607-x/2018016/cpilg-ipcgl-fra.htm

def prix_en_2021(ipc_present, ipc_passe, prix_en_1970):

    prix_en_1970 = float(input("Entrer le prix de l'article en 1970: "))

    return (ipc_present/ipc_passe)*prix_en_1970, prix_en_1970

def nb_heures(salaire_1970, salaire_2021, prix_en_2021):

    heures_trav_70 = prix_70/salaire_1970

    heures_trav_2021 = prix_en_2021/salaire_2021

    return heures_trav_70, heures_trav_2021



IPC_2021 = 138.2
IPC_1970  = 20.2

SALAIRE_MIN_1970 = 1.35
SALAIRE_MIN_2021 = 13.35

prix_21, prix_70 = prix_en_2021(IPC_2021, IPC_1970, prix_en_1970)

heure_travail_70, heure_travail_21 = nb_heures(SALAIRE_MIN_1970, SALAIRE_MIN_2021, prix_21, prix_70)

print(f"Le prix de votre article en 2021 est de {prix_21:.2f}")

print(f"le nombre d'heures requis en 1970 pour cet article est de {heure_travail_70} et est de {heure_travail_21} en 2021.")