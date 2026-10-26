from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configuración de la base de datos (SQLite local)
database_url = os.getenv('DATABASE_URL', 'sqlite:///ecoreto.db')
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de la tabla de Acciones Ecológicas
class Accion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    impacto = db.Column(db.String(100), nullable=False)

with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Error al conectar/crear tablas: {e}")
        
# 1. Ruta de Login (Raíz)
@app.route('/')
def login():
    return render_template('login.html')

# 2. Ruta de la Lista de Acciones
@app.route('/acciones')
def lista_acciones():
    acciones = Accion.query.all()
    return render_template('acciones.html', acciones=acciones)

# 3. Ruta para Nueva Acción (¡Esta era la que faltaba!)
@app.route('/nueva', methods=['GET', 'POST'])
def nueva_accion():
    if request.method == 'POST':
        nueva = Accion(
            fecha=request.form['fecha'],
            tipo=request.form['tipo'],
            descripcion=request.form['descripcion'],
            impacto=request.form['impacto']
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('lista_acciones'))
    return render_template('nueva.html')

# 4. Ruta para Editar Acción
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_accion(id):
    accion = Accion.query.get_or_404(id)
    if request.method == 'POST':
        accion.fecha = request.form['fecha']
        accion.tipo = request.form['tipo']
        accion.descripcion = request.form['descripcion']
        accion.impacto = request.form['impacto']
        db.session.commit()
        return redirect(url_for('lista_acciones'))
    return render_template('editar.html', accion=accion)

# 5. Ruta para Eliminar Acción
@app.route('/eliminar/<int:id>')
def eliminar_accion(id):
    accion = Accion.query.get_or_404(id)
    db.session.delete(accion)
    db.session.commit()
    return redirect(url_for('lista_acciones'))

if __name__ == '__main__':
    app.run(debug=True)



