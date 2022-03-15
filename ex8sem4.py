#Écrire une fonction prenant deux nombres et vérifiant si le premier nombre est plus petit que le deuxième
#si ce n'est pas le cas, les retourner dans l'ordre inverse.
#Ex.: fonction(4, 3) retournerait 3 et, ensuite, 4.

def nombre(nb1, nb2):
   
    ordre = ""
    if nb1 <= nb2:
        ordre = nb1, nb2

    else:
        ordre = nb2, nb1
        
    return ordre

nombre1 = 15
nombre2 = 10

print(nombre(nombre1, nombre2))