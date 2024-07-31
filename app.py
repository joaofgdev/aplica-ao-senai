from flask import Flask, render_template
from asgiref.wsgi import WsgiToAsgi
import pandas as pd
import os

TITULO = os.getenv("TITULO")

app = Flask(__name__)


@app.route("/inicio")
def home():
    df = pd.read_csv("livros.csv")
    lista = df["Titulo do Livro"].tolist()
    return render_template("lista.html", titulo=TITULO, lista_de_livros=lista)


@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")


asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run()
