from flask import Flask
from app.api.api import api_blueprint
from app.main.main import main_blueprint
from app.bookmarks.bookmarks import bookmarks_blueprint

# Initiate Flask app, load config and register blueprints
app = Flask(__name__, static_folder='static')
app.config.from_pyfile('config.py')
app.register_blueprint(main_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(api_blueprint)


if __name__ == '__main__':
    app.run()
