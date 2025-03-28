
def template_return(file):
    try:
        with open(f"static/{file}.html", "r", encoding="utf-8") as fichier:
            fichier_html = "Content-Type: text/html\n\n" + fichier.read()
        return fichier_html
    except FileNotFoundError:
        return "Content-Type: text/html\n\nErreur : fichier introuvable."

def redirect_to(file):
    print(f"""Content-Type: text/html \n
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta http-equiv='refresh' content='0; URL={file}'>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Forum informatique,programation, hacking ...</title>
        </head>
        <body>
        </body>
        </html>
    """)