import cgi
import cgitb
import mysql.connector
import random

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
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="home.py">Home</a></li>
                        <li class="nav-item"><a class="nav-link" aria-current="page" href="listaImmobiliUtente.py">Lista immobili</a></li>
                    </ul>
                    <li class="nav-item"><a class="nav-link" href="index.html">Logout</a></li> 
                </div>
            </div>
        </nav>
        <!-- Header-->
        <header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder">Agenzia Immobiliare</h1>
                    <p class="lead fw-normal text-white-50 mb-0">Acquista la tua casa dei sogni!</p>
                </div>
            </div>
        </header>
      """)

#section -apertura
print("""
        <!-- Section-->
        <section class="py-5">
            <div class="container px-4 px-lg-5 mt-5">
                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
      """)

queryImmobili = "SELECT prezzo, indirizzo FROM immobile"
cursor.execute(queryImmobili)  
immobiliDisponibili = cursor.fetchall()

#print(immobiliDisponibili)

for prezzo, indirizzo in immobiliDisponibili:
    immagineScelta = random.randint(1, 9)
    print(f"""  
                        <div class="col mb-5">
                            <div class="card h-100">
                                <!-- Product image-->
                                <img class="card-img-top" src="img/img{immagineScelta}.jpg" alt="..." />
                                <!-- Product details-->
                                <div class="card-body p-4">
                                    <div class="text-center">
                                        <!-- Product name-->
                                        <h5 class="fw-bolder">{indirizzo}</h5>
                                        <!-- Product price-->
                                        ${prezzo}
                                    </div>
                                </div>
                            </div>
                        </div>
        """)

#section - chiusura
print("""
                </div>
            </div>
        </section>
      """)

#footer
print("""
        <!-- Footer-->
        <footer class="py-5 bg-dark">
            <div class="container"><p class="m-0 text-center text-white">Copyright &copy; Agenzia Immobiliare</p></div>
        </footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="jsHome/scripts.js"></script>
    </body>
</html>

      """)