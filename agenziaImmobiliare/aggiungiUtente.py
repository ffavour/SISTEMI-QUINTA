import cgi
import cgitb
import mysql.connector
import sys


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
        <title>Home </title>
        <!-- Favicon-->
        <link rel="icon" type="image/x-icon" href="assetsHome/favicon.ico" />
        <!-- Bootstrap icons-->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" />
        <!-- Core theme CSS (includes Bootstrap)-->
        <link href="cssHome/styles.css" rel="stylesheet" />
    </head>
    <body>
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container px-4 px-lg-5">
                <a class="navbar-brand" href="#!">Agenzia Immobiliare</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-4">
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="adminPage.py">Home</a></li>
                        <li class="nav-item"><a class="nav-link" href="aggiungiImmobile.py">Aggiungi un immobile</a></li>
                        <li class="nav-item"><a class="nav-link active" href="aggiungiUtente.py">Aggiungi un utente</a></li>
                    </ul>
                    
                </div>
            </div>
        </nav>
        <h1>AGGIUNGI UTENTE</h1>
      """)




#footer
print("""
<!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="jsHome/scripts.js"></script>
    </body>
</html>
      """)