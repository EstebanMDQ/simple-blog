import os, urlparse
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

# import settings

app = Flask(__name__)
app.debug = True
app.config["MONGODB_DB"] = "my_tumble_log"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"


MONGOLAB_URI = os.environ.get('MONGOLAB_URI')
if MONGOLAB_URI:
    url = urlparse.urlparse(MONGOLAB_URI)
    MONGODB_USER = url.username
    MONGODB_PASSWORD = url.password
    MONGODB_HOST = url.hostname
    MONGODB_PORT = url.port
    MONGODB_DB = url.path[1:]


# 



db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)
    
register_blueprints(app)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', port)
