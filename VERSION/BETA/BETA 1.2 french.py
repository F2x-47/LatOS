import os
import platform
from datetime import datetime
from termcolor import colored

fichiers_crees = []

def afficher_aide():
    """Affiche la liste des commandes disponibles."""
    print(colored("\n=== Commandes disponibles ===", 'cyan'))
    print(colored("help", 'yellow') + "          - Afficher cette liste d'aide")
    print(colored("clear", 'yellow') + "         - Effacer l'écran")
    print(colored("date", 'yellow') + "          - Afficher la date et l'heure actuelles")
    print(colored("list", 'yellow') + "          - Afficher la liste des fichiers créés")
    print(colored("create <nom>", 'yellow') + "  - Créer un fichier vide avec le nom spécifié")
    print(colored("write <nom>", 'yellow') + "   - Écrire dans un fichier")
    print(colored("read <nom>", 'yellow') + "    - Lire le contenu d'un fichier")
    print(colored("delete <nom>", 'yellow') + "  - Supprimer un fichier")
    print(colored("calc", 'yellow') + "          - Ouvrir une calculatrice")
    print(colored("exit", 'yellow') + "          - Quitter le système d'exploitation")
    print(colored("=============================\n", 'cyan'))

def effacer_console():
    """Efface l'écran."""
    os.system("cls" if platform.system() == "Windows" else "clear")

def afficher_date():
    """Affiche la date et l'heure actuelles."""
    maintenant = datetime.now()
    print(colored("\n" + maintenant.strftime("%A %d %B %Y à %H:%M:%S").capitalize() + "\n", 'green'))

def lister_fichiers():
    """Affiche la liste des fichiers créés via le système."""
    if fichiers_crees:
        print(colored("\n=== Fichiers créés via LatOS ===", 'cyan'))
        for fichier in fichiers_crees:
            print(colored(f"- {fichier}", 'yellow'))
        print(colored("================================\n", 'cyan'))
    else:
        print(colored("\nAucun fichier créé via LatOS pour le moment.\n", 'red'))

def creer_fichier(nom):
    """Crée un fichier vide."""
    try:
        with open(nom, "x") as f:
            fichiers_crees.append(nom)  # Ajouter le fichier à la liste
            print(colored(f"Fichier '{nom}' créé avec succès.", 'green'))
    except FileExistsError:
        print(colored(f"Erreur : Le fichier '{nom}' existe déjà.", 'red'))

def ecrire_dans_fichier(nom):
    """Écrit dans un fichier."""
    try:
        with open(nom, "a") as f:
            contenu = input(colored("Entrez le texte à écrire dans le fichier : ", 'cyan'))
            f.write(contenu + "\n")
            print(colored(f"Texte ajouté au fichier '{nom}'.", 'green'))
    except FileNotFoundError:
        print(colored(f"Erreur : Le fichier '{nom}' n'existe pas.", 'red'))

def lire_fichier(nom):
    """Lit et affiche le contenu d'un fichier."""
    try:
        with open(nom, "r") as f:
            print(colored(f"\nContenu du fichier '{nom}':", 'cyan'))
            print(f.read())
    except FileNotFoundError:
        print(colored(f"Erreur : Le fichier '{nom}' n'existe pas.", 'red'))

def supprimer_fichier(nom):
    """Supprime un fichier."""
    try:
        os.remove(nom)
        if nom in fichiers_crees:
            fichiers_crees.remove(nom)  # Retirer le fichier de la liste
        print(colored(f"Fichier '{nom}' supprimé avec succès.", 'green'))
    except FileNotFoundError:
        print(colored(f"Erreur : Le fichier '{nom}' n'existe pas.", 'red'))

def calculatrice():
    """Ouvre une calculatrice simple."""
    print(colored("\n=== Calculatrice ===", 'cyan'))
    print(colored("Entrez une opération mathématique (exemple : 5 + 3) ou 'exit' pour quitter.", 'yellow'))
    while True:
        operation = input(colored("calc> ", 'cyan'))
        if operation.lower() == "exit":
            break
        try:
            resultat = eval(operation)
            print(colored(f"Résultat : {resultat}", 'green'))
        except Exception as e:
            print(colored(f"Erreur : {e}", 'red'))

def systeme():
    """Lance LatOS"""
    effacer_console()
    print(colored("Bienvenue dans LatOS !", 'magenta'))
    print(colored("Version de LatOS : BETA 1.3", 'green'))
    print(colored("Tapez 'help' pour voir la liste des commandes disponibles.\n", 'yellow'))

    while True:
        commande = input(colored("> ", 'cyan')).strip()
        if commande == "help":
            afficher_aide()
        elif commande == "clear":
            effacer_console()
        elif commande == "date":
            afficher_date()
        elif commande == "list":
            lister_fichiers()
        elif commande.startswith("create "):
            nom = commande.split(" ", 1)[1]
            creer_fichier(nom)
        elif commande.startswith("write "):
            nom = commande.split(" ", 1)[1]
            ecrire_dans_fichier(nom)
        elif commande.startswith("read "):
            nom = commande.split(" ", 1)[1]
            lire_fichier(nom)
        elif commande.startswith("delete "):
            nom = commande.split(" ", 1)[1]
            supprimer_fichier(nom)
        elif commande == "calc":
            calculatrice()
        elif commande == "exit":
            print(colored("Au revoir !", 'magenta'))
            break
        else:
            print(colored(f"Commande '{commande} inconnue : tapez 'help' pour voir la liste des commandes.", 'red'))

if __name__ == "__main__":
    systeme()
