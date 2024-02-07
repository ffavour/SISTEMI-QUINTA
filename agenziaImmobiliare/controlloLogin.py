import cgi
import cgitb
import mysql.connector
import sys

# Abilita il traceback dettagliato per debug in CGI
cgitb.enable()

try:
    # Connessione al database
    cnx = mysql.connector.connect(user='root', password='Osasere24',
                                  host='127.0.0.1',
                                  database='agenziaImmobiliare')
    cursor = cnx.cursor()

    # Ottieni i dati dalla richiesta CGI
    form = cgi.FieldStorage()
    user = form.getvalue('username')
    password = form.getvalue('pass')

    # Esegui la query SQL parametrizzata
    query = ("SELECT U.username, U.passw, U.ruolo "
             "FROM Utente U, Ruoli R "
             "WHERE U.ruolo = R.id "
             "AND U.username = %s "
             "AND U.passw = %s")
    cursor.execute(query, (user, password))

    # Ottieni i risultati della query
    result = cursor.fetchall()

    # Verifica se l'utente è stato trovato nel database
    if result:
        # L'utente è autenticato correttamente
        print("Content-type: text/html\n")
        print("<h1>Accesso riuscito!</h1>")
        # Effettua il reindirizzamento alla pagina di home
        print(result[0][2]) 
        if result[0][2] == 1:
            print("<meta http-equiv='refresh' content='0;url=http://127.0.0.1:87/adminPage.py'>")
        else:
            print("<meta http-equiv='refresh' content='0;url=http://127.0.0.1:87/home.html'>")
    else:
        # L'utente non è stato trovato nel database
        print("Content-type: text/html\n")
        print("<h1>Accesso non riuscito. Utente non trovato.</h1>")
        print("<meta http-equiv='refresh' content='0;url=http://127.0.0.1:87/index.html'>")
        print("<h1>Accesso non riuscito. Utente non trovato.</h1>")

    # Chiusura del cursore e della connessione
    cursor.close()
    cnx.close()

except mysql.connector.Error as err:
    # Gestione degli errori MySQL
    print("Content-type: text/html\n")
    print(f"<h1>Errore MySQL: {err}</h1>")

except Exception as e:
    # Gestione generica degli errori
    print("Content-type: text/html\n")
    print(f"<h1>Errore generico: {e}</h1>")
