import os
from flask import Flask, render_template
from flask_jsonpify import jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("home.html")


@app.route('/status')
def status():
    return jsonify(status="success", message="successfully completed... NO ERRORS..")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)), debug=True)
