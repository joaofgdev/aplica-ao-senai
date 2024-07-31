from flask import Flask, render_template
from asgiref.wsgi import WsgiToAsgi
import pandas as pd
import os

TITULO = os.getenv("TITULO")

app = Flask(__name__)
app.config['DEBUG'] = True  # Habilitar o modo de depuração

@app.route("/inicio")
def home():
    try:
        df = pd.read_csv("livros.csv")  # Verifique o caminho aqui
        lista = df["Titulo do Livro"].tolist()
    except FileNotFoundError:
        app.logger.error("Arquivo livros.csv não encontrado")
        return "Arquivo livros.csv não encontrado", 404
    except Exception as e:
        app.logger.error(f"Ocorreu um erro ao ler o arquivo CSV: {e}")
        return f"Ocorreu um erro: {e}", 500
    return render_template("lista.html", titulo=TITULO, lista_de_livros=lista)

@app.route("/curriculo")
def curriculo():
    return render_template("curriculo.html")

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    app.run(debug=True)  # Habilitar o modo de depuração
