# Importa la clase Flask desde la biblioteca para crear
# una aplicacion web
from flask import Flask

# Crea una instancia de Flask y utiliza el nombre del modulo actual
# para identificar la aplicacion
app = Flask(__name__)

# Define la ruta principal "/" y la asocia con la funcio que aparece debajo
@app.route("/")

# Declara la funcion inicio que se ejecutara cuando un usuario visite la 
# ruta principal
def inicio():
    # Decuelve el texto que Flask enviara como respuesta al navegador
    return "<h1>¡Hola Mundo desde Docker!</h1>"

# Comprueba directamente si este archivo se esta ejecutando directamente y 
# no importado desde otro archivo
if __name__ == "__main__":
    # Inicia el servidor Flask, escucha en todas las interfaces de red 
    # del contenedor y utiliza el puero 5000
    app.run(host="0.0.0.0", port=5000)
