from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_yeaaa'

@app.route("/inicio")
def index():
    return render_template("index.html")

@app.route("/iniciodesesion", methods=['GET', 'POST'])
def iniciodesesion():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in usuarios and usuarios[email] == password:
            flash('¡Inicio de sesión exitoso!')
            return redirect(url_for('index'))
        else:
            flash('Email o contraseña incorrectos')
    
    return render_template('iniciodesesion.html')

emails_registrados = ["admin@test.com", "usuario@gmail.com"]

usuarios = {
    'admin@test.com': 'admin123',
    'user@test.com': 'user123',
    'gregorio@cetis61.com': 'mi_password'
}

@app.route("/", methods=["GET", "POST"])
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
        usuarios[email] = contraseña
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