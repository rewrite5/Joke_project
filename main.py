#!/usr/bin/env python3
import requests
from colorama import init, Fore


def color():
    print(Fore.GREEN)


def main():
    init()
    params = {"lang": "es", "type": "single"}
    response = requests.get("https://v2.jokeapi.dev/joke/Any", params=params)
    if response.status_code == 200:
        color()
        print("CHISTES ALEATORIOS:")
        diccionario = response.json()
        impresion = {
            "Categoria": diccionario["category"],
            "Tipo": diccionario["type"],
            "Chiste": diccionario["joke"],
        }
        for claves, valores in impresion.items():
            print(claves, ":", valores)
    else:
        print(Fore.RED + f"Ha ocurrido el siguiente Error: {response.status_code}")


if __name__ == "__main__":
    main()
