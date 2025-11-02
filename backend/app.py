from flask import Flask
from application.models import db , User ,Role
from application.config import LocalConfig
from flask_security import Security,SQLAlchemyUserDatastore
def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalConfig)
    db.init_app(app)
    datastore = SQLAlchemyUserDatastore(db , User ,  Role)
    app.security =  Security(app , datastore = datastore)
    app.app_context().push()
    return app

app = create_app()
from application.routes import *
from application.create_initial_data import *
if __name__ == "__main__":
    app.run(debug=True)