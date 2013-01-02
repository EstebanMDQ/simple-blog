import os
from flask import Flask
from flask.ext.mongoengine import MongoEngin
from mongoengine import connect

# import settings

app = Flask(__name__)
app.debug = True
app.config["MONGODB_DB"] = "my_tumble_log"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"


mongo_uri = os.environ.get('MONGOLAB_URI')
app.config["MONGODB_SETTINGS"] = mongo_uri

# {
#     'db': app.config.get('MONGODB_DB', None),
#     'username': app.config.get('MONGODB_USERNAME', None),
#     'password': app.config.get('MONGODB_PASSWORD', None),
#     'host': app.config.get('MONGODB_HOST', None),
#     'port': int(app.config.get('MONGODB_PORT', 0)) or None
# }
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
