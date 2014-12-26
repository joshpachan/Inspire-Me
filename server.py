#! /user/bin/python
from flask import Flask, request, render_template

app = Flask(__name__)

BASE_URI = '/'


@app.route(BASE_URI, methods=["GET"])
def render_home():
    return render_template('index.html')

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()
