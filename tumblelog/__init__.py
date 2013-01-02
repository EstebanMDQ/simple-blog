import os
from flask import Flask
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect

# import settings

app = Flask(__name__)
app.debug = True
app.config["MONGODB_DB"] = "my_tumble_log"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"


mongo_uri = os.environ.get('MONGOLAB_URI')
if mongo_uri :
    parts = mongo_uri.split(":")
    uname = parts[2]
    host = parts[1][2:]
    dbname = parts[3].split('/')[1]
    port = parts[3].split('/')[0] 
    app.config["MONGODB_SETTINGS"] = {
        'db': dbname,
        'username': uname,
        'password': '',
        'host': host,
        'port': port
    }


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
