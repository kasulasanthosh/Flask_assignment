from flask import Flask, render_template, request, abort
import werkzeug

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simulate404")
def simulate404():
    abort(404)
    return render_template("more.html")

@app.route("/simulate500")
def simulate500():
    abort(500)
    return render_template("more.html")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(werkzeug.exceptions.HTTPException)
def internal_error(error):
    return render_template('500.html'), 500

if __name__== "__main__":
    app.run(debug=True)
