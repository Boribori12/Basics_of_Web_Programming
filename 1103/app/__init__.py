from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # @app.route('/')
    # def hello():
    #     return render_template("hello.html")
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app

    