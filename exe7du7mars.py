#Créer une calculatrice d'IMC demandant à l'utilisateur sa grandeur(en mètres), son poids(en kg). Retournez ensuite la catégorie dans laquelle se trouve la personne.

#
def poids_taille(): 

    poids = int(input("Entrer votre poids en kg: "))
    taille = float(input("Entre votre taille en metres: "))

    imc = poids/taille**2
    
    if imc < 18.5:
        categorie = "insuffisance ponderale"
    if imc >= 18.5:
        if imc < 25:
            categorie = "poids normal"
    if imc >= 25:
        if imc < 30:
            categorie = "signe avant-coureur de surpoids"
    if imc >= 30:
        if imc < 35:
            categorie = "obésité niveau 1"
    if imc >= 35:
        if imc < 40:
            categorie = "obésité niveau 2"
    if imc >= 40:
        categorie = "obésité niveau 3"

    return categorie


rep = poids_taille()
print(f"Votre catégorie imc est {rep}")
    


