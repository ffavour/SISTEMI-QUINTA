import cgi
import cgitb
import mysql.connector
import sys

cgitb.enable()
cnx = mysql.connector.connect(user='root', password='Osasere24',
                                  host='127.0.0.1',
                                  database='agenziaImmobiliare')
cursor = cnx.cursor()

print("Content-type: text/html\n")

#header + nav
print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Aggiungi un Utente </title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assetsHome/favicon.ico" />
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="cssHome/styles.css" rel="stylesheet" />
    </head>
    <body>
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#!">Agenzia Immobiliare</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="adminPage.py">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="aggiungiImmobile.py">Aggiungi un immobile</a></li>
                        <li class="nav-item"><a class="nav-link active" href="aggiungiUtente.py">Aggiungi un utente</a></li>
                    </ul>
                    <li class="nav-item" style="color:white;"><a class="nav-link" href="index.html">Logout</a></li>  
                </div>
            </div>
        </nav><br>
        <center><h3>Aggiungi un utente</h3></center>
        <div class="container mt-5">
        <form action="" method="post">
            <div class="form-group">
                <label for="nome">Nome:</label>
                <input type="text" class="form-control" id="nome" name="nome" required>
            </div>

            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" class="form-control" id="username" name="username" required>
            </div>

            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" class="form-control" id="password" name="password" required>
            </div>

            <div class="form-group">
                <label for="ruolo">Ruolo:</label>
                <select class="form-control" id="ruolo" name="ruolo">
                    <option>Seleziona un ruolo</option>
                    <option value="1">Amministratore</option>
                    <option value="2">Utente Normale</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Invia</button>
        </form>
    </div>
      """)




#footer
print("""
<!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="jsHome/scripts.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
</html>
      """)


form = cgi.FieldStorage()
nome = form.getvalue('nome')
username = form.getvalue('username')
password = form.getvalue('password')
ruolo = form.getvalue('ruolo')

try:
    #controlla che username siano univoci
    queryControlloUsername = "SELECT username FROM utente WHERE username = %s"
    cursor.execute(queryControlloUsername, (username,))  
    usernameDisponibili = cursor.fetchall()

    if len(usernameDisponibili) > 0:
        print("username gia' in uso")
    else:  
        # Query SQL di inserimento
        query = ("INSERT INTO utente (nome, username, passw, ruolo) "
                "VALUES (%s, %s, %s, %s)")
                
        values = (nome, username, password, ruolo)
        cursor.execute(query, values)
        cnx.commit()

        cursor.close()
        cnx.close()
        print("Record inserito correttamente.")

except mysql.connector.Error as err:
    # Gestione degli errori MySQL
    print(f"Errore MySQL: {err}")

except Exception as e:
    # Gestione generica degli errori
    print(f"Errore generico: {e}")
