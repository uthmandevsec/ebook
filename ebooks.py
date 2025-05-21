# ebooks.py

# Générateur de contenu simple avec des modèles de phrases pré-écrites.
# Pas d'IA sophistiquée, juste un mélange aléatoire de phrases.

import random

# Titres d’ebooks générés
def generate_titles():
    # Liste fixe de titres à combiner aléatoirement
    adjectives = ["Mystérieux", "Enchanté", "Ombre", "Lumière", "Secret"]
    nouns = ["Voyage", "Forêt", "Étoile", "Rêve", "Château"]
    titles = []
    for i in range(5):
        # Compose un titre avec un adjectif + un nom, ex : "Lumière du Château"
        title = f"{random.choice(adjectives)} {random.choice(nouns)}"
        titles.append(title)
    return titles

# Contenu simple généré pour chaque ebook
def generate_content(title):
    # Quelques phrases types à répéter pour simuler du contenu
    sentences = [
        f"Bienvenue dans le livre intitulé '{title}'.",
        "Ce livre vous emmène dans un voyage incroyable à travers des mondes fascinants.",
        "Chaque chapitre révèle un secret unique qui vous captivera.",
        "Préparez-vous à découvrir des personnages fascinants et des aventures inoubliables.",
        "Merci d'avoir choisi ce livre, bonne lecture !"
    ]
    # Retourne plusieurs paragraphes
    content = "\n\n".join(sentences)
    return content


# Générer la liste complète d’ebooks
def generate_ebooks():
    ebooks = []
    titles = generate_titles()
    for title in titles:
        ebook = {
            "title": title,
            "content": generate_content(title)
        }
        ebooks.append(ebook)
    return ebooks
