import requests
import json
import sys


###############
## FUNCTIONS ##
###############

def divide(x, y):
    if y > 0:
        return x / y
    else:
        return "not able to divide 0"


def menu():
    print("Calculadora de cotizacion del dolar del dia.")
    print("------------------------------------")
    print("1.Obtener el valor a Dolar oficial.")
    print("2.Obtener el valor a Dolar blue.")
    print("Cualquier otro numero: Exit")
    print("------------------------------------")


def get_dolar_value(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        data = respuesta.json()
        dolar_value = json.dumps(data['venta'], indent=4)
        dolar_value = float(dolar_value.replace('"', ''))
    return dolar_value


def add_input(msg):
    n = float(input(msg))
    return n


def calculate_dolar(num1, num2, choice):
    if choice == 1:
        result = divide(num1, num2)
    if choice == 2:
        result = divide(num1, num2)
    return result


###############
##   MAIN    ##
###############

if __name__ == '__main__':

    while True:
        menu()

        choice = add_input("Elegi tu opcion(1/2): ")
        valid_options = [1, 2]
        result = 0

        if choice in valid_options:
            num1 = add_input("Ingresa los pesos a convertir: ")

            if choice == 1:
                url_dolar = 'http://api-dolar-argentina.herokuapp.com/api/dolaroficial'

            if choice == 2:
                url_dolar = 'http://api-dolar-argentina.herokuapp.com/api/dolarblue'

            num2 = get_dolar_value(url_dolar)

            calculate_dolar_result = calculate_dolar(num1, num2, choice)
            calculate_dolar_result = round(calculate_dolar_result, 2)
        else:
            sys.exit("Bye Bye!")

        print(f"\nLa cantidad de dolares es: {calculate_dolar_result}\n")
