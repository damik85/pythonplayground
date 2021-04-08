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

url = 'http://api-dolar-argentina.herokuapp.com/api/dolaroficial'
respuesta = requests.get(url)
if respuesta.status_code == 200:
    data = respuesta.json()
    num2 = json.dumps(data['venta'], indent=4)
    num2 = float(num2.replace('"', ''))

url = 'http://api-dolar-argentina.herokuapp.com/api/dolarblue'
respuesta = requests.get(url)
if respuesta.status_code == 200:
    data = respuesta.json()
    num3 = json.dumps(data['venta'], indent=4)
    num3 = float(num3.replace('"', ''))

def add_input(msg):
    n = float(input(msg))
    return n

def calculate_dolar(num1, num2, choice):
    if choice == 1:
        result = divide(num1, num2)
    if choice == 2:
        result = divide(num1, num3)
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
            calculate_dolar_result = calculate_dolar(num1, num2, choice)
            calculate_dolar_result = round(calculate_dolar_result, 2)
        else:
            sys.exit("Bye Bye!")

        print(f"\nLa cantidad de dolares es: {calculate_dolar_result}\n")