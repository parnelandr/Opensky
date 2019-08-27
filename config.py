import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

# create the connexion app instance
connex_app = connexion.App(__name__, specification_dir=basedir)

#get flask app instance
app = connex_app.app

# config SQLAlchemy
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'position.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#SQLAlchemy db instance
db = SQLAlchemy(app)

#Initialise Marshmallow
ma = Marshmallow(app)