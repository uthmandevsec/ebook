# app.py

from flask import Flask, render_template, send_file, request, redirect, url_for
import os
from ebooks import generate_ebooks
import pyttsx3  # Synthèse vocale locale
import uuid    # Pour noms de fichiers uniques
import builtins
app = Flask(__name__)

# Génère 5 ebooks au démarrage
ebooks = generate_ebooks()

# Crée le dossier audio s'il n'existe pas
os.makedirs("static/audio", exist_ok=True)

@app.route("/")
def index():
    # on passe ebooks + enumerate dans le template
    return render_template("index.html", ebooks=ebooks, enumerate=enumerate)

@app.route("/download/<int:ebook_id>")
def download_ebook(ebook_id):
    # Permet de télécharger le contenu ebook en format texte
    if 0 <= ebook_id < len(ebooks):
        ebook = ebooks[ebook_id]
        # Création d'un fichier texte temporaire
        filename = f"{ebook['title'].replace(' ', '_')}.txt"
        filepath = os.path.join("static", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(ebook['content'])
        # Envoi du fichier en téléchargement
        return send_file(filepath, as_attachment=True)
    return "Livre non trouvé", 404

@app.route("/listen/<int:ebook_id>")
def listen_ebook(ebook_id):
    # Génère un fichier MP3 avec la synthèse vocale du contenu ebook
    if 0 <= ebook_id < len(ebooks):
        ebook = ebooks[ebook_id]
        # Initialise le moteur TTS
        engine = pyttsx3.init()
        # Génère un nom de fichier unique
        audio_filename = f"{uuid.uuid4()}.mp3"
        audio_path = os.path.join("static", "audio", audio_filename)
        # Sauvegarde le texte en MP3
        engine.save_to_file(ebook['content'], audio_path)
        engine.runAndWait()
        # Redirige vers la page principale avec le son prêt
        return redirect(url_for("index", audio=audio_filename))
    return "Livre non trouvé", 404

if __name__ == "__main__":
    app.run(debug=True)
