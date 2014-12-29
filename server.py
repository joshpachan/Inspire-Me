#!/usr/bin/python
from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

BASE_URI = '/'
QUOTE_DEFAULT = 'Are you ready for it?'

@app.route(BASE_URI, methods=["GET"])
def render_home():
    return render_template('index.html', quote=QUOTE_DEFAULT)

@app.route(BASE_URI +'hit-me', methods=["GET"])
def change_text():
    # api_url = 'http://theysaidso.com/api/v1.0/random.json?category=inspiration'
    # req = request(api_url)
    new_quote = "NAH YOU AIN'T READY FOR IT."
    return render_template('index.html', quote=new_quote)

def main():
    app.run()

if __name__ == "__main__":
    main()
