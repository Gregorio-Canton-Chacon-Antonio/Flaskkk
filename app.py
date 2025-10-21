from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_yeaaa'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/inicio")
def inicio():
    return render_template("iniciodesesion.html")

emails_registrados = ["admin@test.com", "usuario@gmail.com"]

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellidos = request.form.get("apellidos")
        email = request.form.get("email")
        contraseña = request.form.get("contraseña")
        confirmAcontraseña = request.form.get("confirmAcontraseña")
        
        if email in emails_registrados:
            flash("Este correo electrónico ya está registrado")
            return render_template("formulario.html")
        
        if contraseña != confirmAcontraseña:
            flash("Las contraseñas no coinciden")
            return render_template("formulario.html")
        
        emails_registrados.append(email)
        flash(f"Registro exitoso para {nombre} {apellidos}!")
        return redirect(url_for('index'))
    
    return render_template("formulario.html")




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