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

print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Home </title>
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
                        <li class="nav-item"><a class="nav-link active" href="aggiungiImmobile.py">Aggiungi un immobile</a></li>
                        <li class="nav-item"><a class="nav-link" href="aggiungiUtente.py">Aggiungi un utente</a></li>
                    </ul>
                    <li class="nav-item" style="color:white;"><a class="nav-link" href="index.html">Logout</a></li>  
                </div>
            </div>
        </nav><br>
        <center><h3>Aggiungi un immobile</h3></center>
      """)


#form inserimento dati immobile
print("""
<div class="container mt-5">
        <form action="" method="post">
            <div class="form-group">
                <label for="indirizzo">Indirizzo:</label>
                <input type="text" class="form-control" id="indirizzo" name="indirizzo">
            </div>

            <div class="form-group">
                <label for="numero_vani">Numero Vani:</label>
                <input type="number" class="form-control" id="numero_vani" name="numero_vani" min="1">
            </div>

            <div class="form-group">
                <label for="metratura">Metratura:</label>
                <input type="number" class="form-control" id="metratura" name="metratura" min="1">
            </div>

            <div class="form-group">
                <label for="piano">Piano:</label>
                <input type="number" class="form-control" id="piano" name="piano" min="1">
            </div>

            <div class="form-group">
                <label for="ascensore">Ascensore:</label>
                <select class="form-control" id="ascensore" name="ascensore">
                    <option value="Si">Si</option>
                    <option value="No">No</option>
                </select>
            </div><br>

            <div class="form-group">
                <label for="prezzo">Prezzo:</label>
                <input type="number" class="form-control" id="prezzo" name="prezzo" min="1">
            </div>

            <div class="form-group">
                <label for="venduto">Venduto:</label>
                <select class="form-control" id="venduto" name="venduto">
                    <option value="Si">Si</option>
                    <option value="No">No</option>
                </select>
            </div>
      """)

#query per select agenzia
queryAgenzie = ("SELECT DISTINCT Ind "
                "FROM agenzia")
cursor.execute(queryAgenzie)
agenzie = cursor.fetchall()


#select agenzia
print("""
<div class="form-group">
                <label for="agenzia">Agenzia:</label>
                <select class="form-control" id="agenzia" name="agenzia">
                    <option>Seleziona un'agenzia</option>
      """)

for row in agenzie:

    print(f"<option value='{row[0]}'>{row[0]}</option>")

print("""
    </select>
</div><br>
      """)



#query per select localita
queryLocalita = ("SELECT nome "
        "FROM localita")
cursor.execute(queryLocalita)
localitaQ = cursor.fetchall()


#select località
print("""
<div class="form-group">
                <label for="localita">Localita':</label>
                <select class="form-control" id="localita" name="localita">
                    <option>Seleziona una localita'</option>
      """)

for row in localitaQ:

    print(f"<option value='{row[0]}'>{row[0]}</option>")

print("""
    </select>
</div>
<br>
      """)

#chiusura form
print("""
            <button type="submit" class="btn btn-primary">Invia</button>
        </form>
    </div>
      """)


print("""
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <script src="jsHome/scripts.js"></script>
    </body>
</html>
      """)



form = cgi.FieldStorage()
indirizzo = form.getvalue('indirizzo')
numero_vani = form.getvalue('numero_vani')
metratura = form.getvalue('metratura')
piano = form.getvalue('piano')
ascensore = form.getvalue('ascensore')
prezzo = form.getvalue('prezzo')
venduto = form.getvalue('venduto')
agenzia = form.getvalue('agenzia')
localita = form.getvalue('localita')

#print(indirizzo, numero_vani, metratura, piano, ascensore, prezzo, venduto, agenzia, localita)

#query per id agenzia
queryIdAgenzia = ("SELECT id_agenzia "
                "FROM agenzia "
                f"WHERE Ind = '{agenzia}' LIMIT 1")
cursor.execute(queryIdAgenzia)
idAgenzia = cursor.fetchall()
#print(idAgenzia[0][0])

#query per id localita
queryIdLocalita = ("SELECT id_loc "
                "FROM localita "
                f"WHERE nome = '{localita}'")
cursor.execute(queryIdLocalita)
idLocalita = cursor.fetchall()
#print(idLocalita[0][0])

try:
    # Query SQL di inserimento
    query = ("INSERT INTO immobile (indirizzo, nvani, metratura, piano, ascensore, prezzo, Venduto, agenzia, localita) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
             
    values = (indirizzo, numero_vani, metratura, piano, ascensore, prezzo, venduto, idAgenzia[0][0], idLocalita[0][0])
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

