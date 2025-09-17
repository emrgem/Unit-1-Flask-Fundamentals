from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return f"""<h2>Query Parameters </h2
            <ul>
                    <li><a href="/search?q=python&page=2">/search?q=python&page=2</a></li>
            </ul>
"""


if __name__ == "__main__":
    app.run(debug=True)
