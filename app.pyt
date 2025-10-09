from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/animalesexoticos")
def animales():
    return render_template("animales.html")

@app.route("/vehiculosantiguos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/lasmaravillasdelmundo")
def maravillas():
    return render_template("maravillas.html")

@app.route("/acercade")
def acercade():
    return render_template("acercade.html")

if __name__ == "__main__":
    app.run(debug=True)