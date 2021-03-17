import os

from flask import current_app, Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    context = {
        "name": name
    }
    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
