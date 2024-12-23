  import random

def jouer():
    choix_possibles = ["pierre", "feuille", "ciseaux"]
    print("Bienvenue dans le jeu Pierre-Feuille-Ciseaux!")
    
    while True:
        joueur = input("Faites votre choix (pierre, feuille, ciseaux ou quitter): ").lower()
        if joueur == "quitter":
            print("Merci d'avoir joué ! À bientôt !")
            break
        if joueur not in choix_possibles:
            print("Choix invalide. Essayez encore.")
            continue
        
        ordinateur = random.choice(choix_possibles)
        print(f"L'ordinateur a choisi: {ordinateur}")

        if joueur == ordinateur:
            print("Égalité!")
        elif (joueur == "pierre" and ordinateur == "ciseaux") or \
             (joueur == "feuille" and ordinateur == "pierre") or \
             (joueur == "ciseaux" and ordinateur == "feuille"):
            print("Vous gagnez!")
        else:
            print("Vous perdez!")
        print()

# Lancer le jeu
jouer()
