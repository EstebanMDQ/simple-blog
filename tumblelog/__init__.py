from flask import Flask
import flask.ext.mongoengine as mongoengine

app = Flask(__name__)
app.debug = True
app.config["MONGODB_DB"] = "my_tumble_log"
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

mongoengine.connect('mydata', host=os.environ.get('MONGOLAB_URI'))

db = mongoengine.MongoEngine(app)

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
