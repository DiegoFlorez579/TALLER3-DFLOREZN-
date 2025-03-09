from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_user, login_required, current_user, logout_user
from models.models import Usuarios, Perros

routes = Blueprint('routes', __name__)


@routes.route("/")
def index():
    return f"Bienvenido, {'invitado' if not current_user.is_authenticated else current_user.username}!"


@routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)  
            return redirect(url_for('routes.index'))
    return render_template('login.html')


@routes.route('/panel_perros')
@login_required
def panel_perros():
    perros = Perros.query.all()
    if current_user.es_admin:
        return render_template('panel_perros.html', perros = perros)
    else:
        return redirect(url_for('routes.index'))


@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))