from flask import Blueprint, render_template

bp = Blueprint("main", __name__, url_prefix = '/')

# testbp = Blueprint("testbp", __name__, url_prefix = '/')

@bp.route('/')
def hello():
    return render_template("hello.html", name = 'everyone')

@bp.route('/steve')
def hello_steve():
    return render_template("hello.html", name = 'Steve')
