from flask import Flask
from application.models import db , User ,Role
from application.config import LocalConfig
from flask_security import Security,SQLAlchemyUserDatastore
from flask_cors import CORS
def create_app():
    app = Flask(__name__ , template_folder = "../frontend_cdn" , static_folder="../frontend_cdn")
    app.config.from_object(LocalConfig)
    db.init_app(app)
    CORS(app)
    datastore = SQLAlchemyUserDatastore(db , User ,  Role)
    app.security =  Security(app , datastore = datastore , register_blueprint = False)
    @app.security.unauthn_handler
    def unauthn_handler( mechanisms=None, headers=None):
        print(mechanisms)
        return {"message" : "Auth required"} , 401
    
    @app.security.unauthz_handler
    def unauthz_handler( func , params):
        return {"message" : "You do not have access to this resource"} , 403
    app.app_context().push()
    return app

app = create_app()
from application.routes import *
from application.create_initial_data import *
if __name__ == "__main__":
    app.run(debug=True)