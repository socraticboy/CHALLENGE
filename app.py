#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console when the application starts
print("hello world")

# Create a code where when y run app.py, it runs the game rock, paper, scissors and it shows the result in the browser

import random

def jugar():
    opciones = ["rock", "paper", "scissors"]
    victorias = 0
    rondas = 0

    while True:
        print("Elige una opción: rock, paper, scissors")
        jugador = input().lower()

        if jugador not in opciones:
            print("Opción no válida. Inténtalo de nuevo.")
            continue

        oponente = random.choice(opciones)

        # Lógica para determinar el resultado de la ronda
        if jugador == oponente:
            print("Empate!")
        elif (jugador == "rock" and oponente == "scissors") or \
             (jugador == "scissors" and oponente == "paper") or \
             (jugador == "paper" and oponente == "rock"):
            print(f"Ganaste! {jugador} vence a {oponente}")
            victorias += 1
        else:
            print(f"Perdiste! {oponente} vence a {jugador}")

        rondas += 1

        # Preguntar al jugador si desea jugar de nuevo
        print("¿Quieres jugar de nuevo? (s/n)")
        respuesta = input().lower()
        if respuesta != "s":
            break

    print(f"Fin del juego. Tu puntuación: {victorias} victorias de {rondas} rondas.")

if __name__ == "__main__":
    jugar()

