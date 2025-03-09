from flask import Flask
from models.models import db
from views.routes import routes
from config.config import *
from flask_login import LoginManager
from models.models import Usuarios


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))

app.register_blueprint(routes)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)