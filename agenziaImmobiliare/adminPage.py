import cgi
import cgitb
import mysql.connector
import sys

cgitb.enable()
cnx = mysql.connector.connect(user='root', password='Osasere24',
                                  host='127.0.0.1',
                                  database='agenziaImmobiliare')

#query per select localita
cursor = cnx.cursor()
queryLocalita = ("SELECT nome "
        "FROM localita")
cursor.execute(queryLocalita)
localita = cursor.fetchall()




print("Content-type: text/html\n")

# header + navbar
print("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
        <meta name="description" content="" />
        <meta name="author" content="" />
        <title>Admin Page </title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assetsHome/favicon.ico" />
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
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
                        <li class="nav-item"><a class="nav-link active" aria-current="page" href="adminPage.py">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="aggiungiImmobile.py">Aggiungi un immobile</a></li>
                        <li class="nav-item"><a class="nav-link" href="aggiungiUtente.py">Aggiungi un utente</a></li>
                    </ul>
                    <li class="nav-item" style="color:white;"><a class="nav-link" href="index.html">Logout</a></li>  
                </div>
            </div>
        </nav>
      """)

# bottoni in alto
print("""
      <br>
<center><h3>Ciao Admin!</h3></center>
      <div class="filter">
        <form action="" method="post">
            <label for="citta">Citta'</label>
            <select name="citta" id="">
                <option>Seleziona una citta'</option>

      """)


for row in localita:

    print(f"<option value='{row[0]}'>{row[0]}</option>")

print("""
      
      </select>

            <label for="ascensore">Ascensore: </label>
            <select name="ascensore" id="">
                <option value="si">SI</option>
                <option value="no">NO</option>
            </select>

            <input type="submit" name="btnFilter" value="Filtra">
            <input type="submit" name="btnClear" value="Ripristina">
        </form>
    </div><br>

      """)

form = cgi.FieldStorage()
citta = form.getvalue('citta')
ascensore = form.getvalue('ascensore')
btnClear = form.getvalue('btnClear')

#print(citta, ascensore, btnClear)

#tabella
print("""
<table class="table">
      <thead>
        <tr>
            <th scope="col">Indirizzo</th>
            <th scope="col">Numero Vani</th>
            <th scope="col">Metratura</th>
            <th scope="col">Piano</th>
            <th scope="col">Ascensore</th>
            <th scope="col">Prezzo</th>
            <th scope="col">Venduto</th>
            <th scope="col">Agenzia</th>
            <th scope="col">Localita'</th>
        </tr>
        </thead>
        <tbody>
        <!--ciclo for va qui-->
    
      """)

# controlla i filtri
if citta == None and ascensore == None or btnClear == 'Ripristina':
    queryTabella = ("SELECT I.indirizzo, I.nVani, I.metratura, I.piano, I.ascensore, I.prezzo, I.venduto, A.Ind, L.nome "
                "FROM immobile I, localita L, agenzia A "
                "WHERE I.localita = L.id_loc AND A.id_agenzia = I.agenzia")
else:
    queryTabella = ("SELECT I.indirizzo, I.nVani, I.metratura, I.piano, I.ascensore, I.prezzo, I.venduto, A.Ind, L.nome "
                "FROM immobile I, localita L, agenzia A "
                f"WHERE I.localita = L.id_loc AND A.id_agenzia = I.agenzia AND L.nome = '{citta}' and I.ascensore = '{ascensore}'")
cursor.execute(queryTabella)
immobili = cursor.fetchall()

for indirizzo, nvani, metratura, piano, ascensore, prezzo, venduto, agenzia, localita in immobili:
    print(f"""
        <tr>
            <td>{indirizzo}</td>
            <td>{nvani}</td>
            <td>{metratura}</td>
            <td>{piano}</td>
            <td>{ascensore}</td>
            <td>{prezzo}</td>
            <td>{venduto}</td>
            <td>{agenzia}</td>
            <td>{localita}</td>
        </tr>
          """)
print("<tbody></table>")


#footer
print("""
            <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="jsHome/scripts.js"></script>
    </body>
</html>
      """)