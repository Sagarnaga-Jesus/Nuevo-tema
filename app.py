from flask import Flask

app = Flask(__name__)

@app.route('/')
def Calculadora():
    return '''<h1>Bienvenido a la calculadora en python</h1>
                <p>1. Para sumar escribe en el navegador 127.0.0.1:5000/suma/primer numero/segundo numero</p>
                <p>2. Para restar escribe en el navegador 127.0.0.1:5000/resta/primer numero/segundo numero</p>
                <p>3. Para multiplicar escribe en el navegador 127.0.0.1:5000/multiplicacion/primer numero/segundo numero</p>
                <p>4. Para dividir escribe en el navegador 127.0.0.1:5000/division/primer numero/segundo numero</p>
                <p>5. Para diferencia escribe en el navegador 127.0.0.1:5000/diferencia/primer numero/segundo numero</p>
                
                <p> Mi nomnre: Sagarnaga Macias Jesus Antonio 
                    Grupo: 5-D</p>
'''

@app.route('/otra')
def hola_mundo1():
    return '<h1>¡Hola Mundo desde otra ruta !<h1>'

@app.route('/otra2')
def texto():
    return  '''<h1>Mi nuevo tema</h1>
    <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit.
            Nihil dolorem unde, et omnis obcaecati rerum inventore deserunt, 
            sint est iure cupiditate quas repellat doloremque alias odit odio. Quidem, dicta voluptatem.
            Lorem ipsum dolor sit amet consectetur adipisicing elit. 
            Quos, iste debitis in, nam praesentium vitae doloribus animi esse ex aperiam repudiandae laboriosam provident alias eligendi pariatur. 
            Officiis libero architecto quibusdam!</p>
            
            '''

@app.route('/factoria/<v1>')
def factorial(v1):
    f=1
    for x in range(1,int(v1)+1):
        f*=x
    return (f"El factorial de {v1} es: {f}")

@app.route('/suma/<n1>/<n2>')
def suma(n1,n2):
    numero1 = int(n1)
    numero2 = int(n2)
    resultado = numero1+numero2 
    return (f"El resultado de {n1} y {n2} es: {resultado}")

@app.route('/resta/<n1>/<n2>')
def resta(n1,n2):
    numero1 = int(n1)
    numero2 = int(n2)
    resultado = numero1-numero2 
    return (f"El resultado de {n1} y {n2} es: {resultado}")

@app.route('/division/<n1>/<n2>')
def division(n1,n2):
    numero1 = int(n1)
    numero2 = int(n2)
    resultado = numero1/numero2 
    return (f"El resultado de {n1} y {n2} es: {resultado}")

@app.route('/multiplicar/<n1>/<n2>')
def multiplicar(n1,n2):
    numero1 = int(n1)
    numero2 = int(n2)
    resultado = numero1*numero2 
    return (f"El resultado de {n1} y {n2} es: {resultado}")

@app.route('/diferencia/<n1>/<n2>')
def diferencia(n1,n2):
    numero1 = int(n1)
    numero2 = int(n2)
    if numero1 > numero2:
        return (f"El número mayor es: {numero1} y el numero menor es {numero2}")
    else:
        return (f"El número mayor es: {numero2} y el numero menor es {numero1}")



if __name__ == '__main__':
    app.run(debug=True)
