from flask import Flask, render_template, url_for, request, redirect

from . import match, search


def create_app():
    app = Flask(__name__)

    @app.route("/")
    # def hello():
    #     return "Hello World!"
    
    def index():
        return render_template('index.html')
    
    app.register_blueprint(match.bp)
    app.register_blueprint(search.bp)


    return app
