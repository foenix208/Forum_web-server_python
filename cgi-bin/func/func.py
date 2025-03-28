
def template_return(file):
    try:
        with open(f"static/{file}.html", "r", encoding="utf-8") as fichier:
            fichier_html = "Content-Type: text/html\n\n" + fichier.read()
        return fichier_html
    except FileNotFoundError:
        return "Content-Type: text/html\n\nErreur : fichier introuvable."
