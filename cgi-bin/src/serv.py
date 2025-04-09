def ft_redirect(file):
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

def ft_value(file,name,value):
    return file.replace(f"^^{name}",value)

def ft_return_template(file,type=0):
    try:
        with open(f"template/{file}.html", "r", encoding="utf-8") as fichier:
            html =" "
            if type == 0:
                html = "Content-Type: text/html \n\n"

            for i in fichier.readlines():
                if "^$include" in i:
                    html += ft_return_template(i.split(":")[1].split(".")[0],1)
                else:
                    html += i
        return html
    except FileNotFoundError:
        if type == 0:
            return "Content-Type: text/html\n\nErreur : fichier introuvable."
        return "Fichier introuvable. "