"""" Le jeu du Tic Tac Toe (Morpion)

Le jeu du Tic Tac Toe consiste à remplir un tableau composé de neuf cases constituant un carré. Deux joueurs s'affrontent en jouant chacun leur tour. Au début du jeu, le premier joueur choisi un symbole. Soit le symbole "x", soit le symbole "o". Puis chacun son tour, les deux joueurs posent sur la grille leur symbole respectif. Le jeu s'arrête lorsque un des deux joueurs a trois symboles identiques alignés sur une même ligne. Que cela soit de manière verticale, horizontale, ou diagonale.

Explications :
case_de_la_grille = correspond à chaque case de la grille. En tout cela fait neuf cases.
choix_joueur = A chaque partie, un des deux joueurs choisi soit le symbole "x", soit le symbole "o". La grille s'affiche ensuite.
affich_grille = Affiche la grille avec les neufs cases vides à remplir avec les symboles ainsi que la grille secondaire qui informe le numéro des cases à remplir.
vérifier_victoire = Vérifie toutes les combinaisons possibles pour gagner.
Tour_joueur = chaque joueur choisi un chiffre pour remplir la case correspondante. Par exemple, Si un joueur choisi une case déjà selectionné, un message s'affiche 'cette case est déjà prise. Réessayez'



"""

# Initialisation de la grille
case_de_la_grille = ["-","-","-","-","-","-","-","-","-"]

#réinitialisation de la grille à chaque tour
def renitia_grille():
    global case_de_la_grille
    case_de_la_grille = ["-","-","-","-","-","-","-","-","-"]



# Choix du joueur
def choix_joueur():
    global joueur_actuel, joueur_adverse
    joueur_actuel = input("Veuillez choisir soit une croix (x), soit un rond (o) : ").lower()
    if joueur_actuel == "x":
        joueur_adverse = "o"
        print("Vous avez choisi x. Le joueur 2 aura o.")
    elif joueur_actuel == "o":
        joueur_adverse = "x"
        print("Vous avez choisi o. Le joueur 2 aura x.")
    else:
        print("Entrée invalide. Veuillez choisir entre 'x' et 'o'.")
        choix_joueur()

# Affichage de la grille
def affich_grille():
    print("\n")
    print("-------------")
    print("|",case_de_la_grille[0],"|",case_de_la_grille[1],"|",case_de_la_grille[2],"|           | 1 | 2 | 3 |")
    print("-------------")
    print("|",case_de_la_grille[3],"|",case_de_la_grille[4],"|",case_de_la_grille[5],"|           | 4 | 5 | 6 |")
    print("-------------")
    print("|",case_de_la_grille[6],"|",case_de_la_grille[7],"|",case_de_la_grille[8],"|           | 7 | 8 | 9 |")
    print("-------------")
    print("\n")

# Vérifier si un joueur a gagné
def verifier_victoire(symbole):
    # Combinaisons gagnantes
    combinaisons = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonnes
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for comb in combinaisons:
        if case_de_la_grille[comb[0]] == case_de_la_grille[comb[1]] == case_de_la_grille[comb[2]] == symbole:
            return True
    return False

# Vérifier si la grille est pleine
def grille_pleine():
    return "-" not in case_de_la_grille

# Tour de jeu
def tour_joueur(symbole):
    while True:
        try:
            choix = int(input(f"Joueur {symbole}, choisissez une case (1-9) : ")) - 1
            if choix < 0 or choix > 8:
                print("Le choix doit être entre 1 et 9. Réessayez.")
            elif case_de_la_grille[choix] != "-":
                print("Cette case est déjà prise. Réessayez.")
            else:
                case_de_la_grille[choix] = symbole
                break
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entre 1 et 9.")

# Fonction principale du jeu
def jeu():
    choix_joueur()
    renitia_grille()
    affich_grille()
    global joueur_actuel, joueur_adverse
    while True:
        tour_joueur(joueur_actuel)
        affich_grille()
        if verifier_victoire(joueur_actuel):
            print(f"Félicitations ! Joueur {joueur_actuel} a gagné !")
            jeu()
        if grille_pleine():
            print("Match nul ! La grille est pleine.")
            jeu()
        # Changer de joueur
        joueur_actuel, joueur_adverse = joueur_adverse, joueur_actuel

# Lancer le jeu
jeu()