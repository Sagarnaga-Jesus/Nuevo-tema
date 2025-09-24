from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '<h1>¡Hola Mundo desde Flask!<h1>'

@app.route('/otra')
def hola_mundo1():
    return '<h1>¡Hola Mundo desde otra ruta !<h1>'

if __name__ == '__main__':
    app.run(debug=True)