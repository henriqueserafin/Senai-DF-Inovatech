from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("top10_imigrantes2.html")



if __name__ == "__main__":
    app.run(debug=True, port=5001)
