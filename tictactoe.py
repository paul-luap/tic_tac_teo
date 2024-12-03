#définir le tour du joueur



def choix_joueur():
    global joueur_actuel
    joueur_actuel = input("Veuillez choisir soit une croix (x), soit un rond (O) : ")
    if joueur_actuel == "x" :
        print("Vous avez choisi x. Le joueur 2 aura O")
    elif joueur_actuel == "o" :
        print("Vous avez choisi o. Le joueur 2 aura x")
    else:
        choix_joueur()
            

choix_joueur()



#pour afficher la grille

case_de_la_grille = ["-","-","-","-","-","-","-","-","-"]

def affich_grille():
    print("\n")
    print("-------------")
    print("|",case_de_la_grille[0],"|",case_de_la_grille[1],"|",case_de_la_grille[2],"|")
    print("-------------")
    print("|",case_de_la_grille[3],"|",case_de_la_grille[4],"|",case_de_la_grille[5],"|")
    print("-------------")
    print("|",case_de_la_grille[6],"|",case_de_la_grille[7],"|",case_de_la_grille[8],"|")
    print("-------------")
    print("\n")



def jouer():
    while True:
        affich_grille()
        x = input()
jouer()