from flask import Flask, render_template

app = Flask(__name__)

@app.route("/1")
def index():
    arr = ["Luis", "Paco", "Rosita", "Martin", "Elsa"]
    autor = "Antonio Gregorio Canton Chacon"
    return render_template("index.html", nombre = autor, amigos = arr)

@app.route("/2")
def indexx():
    arr = ["1", "2", "3", "4", "5"]
    autor = "Antonio Gregorio Canton Chacon"
    return render_template("indexx.html", nombre = autor, numeros = arr)

@app.route("/3")
def indexxx():
    arr = ["Wolf", "Cherry Bomb", "Flower Boy", "IGOR", "CMIYGL"]
    autor = "Antonio Gregorio Canton Chacon"
    return render_template("indexxx.html", nombre = autor, albumes = arr)

@app.route("/4")
def indexxxx():
    arr = ["1", "2", "3", "4", "5"]
    autor = "Antonio Gregorio Canton Chacon"
    return render_template("indexxxx.html", nombre = autor, juegos = arr)

if __name__ == "__main__":
    app.run(debug=True)