from flask import Flask, render_template, request

app = Flask(__name__)

# Función para convertir grados Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
   fahrenheit = (celsius * 9/5) + 32
   return fahrenheit

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       try:
           celsius = float(request.form['celsius'])
           fahrenheit = celsius_a_fahrenheit(celsius)
           return render_template('resultado.html', celsius=celsius, fahrenheit=fahrenheit)
       except ValueError:
           error_message = "Ingresa una temperatura válida en grados Celsius."
           return render_template('index.html', error_message=error_message)

   return render_template('index.html')

if __name__ == '__main__':
   app.run()
