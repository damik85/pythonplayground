# MENU E INGRESO DE DATOS
operation = str(input("Ingresar opcion 1.Suma 2.Resta 3.Multiplicacion 4.Division 5.Salir: "))

# Loop de salida
while operation != 5:

    # Ingreso los valores a calcular
    value1 = int(input('Insert Value 1: '))
    value2 = int(input('Insert Value 2: '))

    # SUMA
    if operation == "1":
        resultsuma = (value1 + value2)
        print("El resultado de la suma es: ", int(resultsuma))

    # RESTA
    elif operation == "2":
        resultresta = (value1 - value2)
        print("El resultado de la resta es: ", int(resultresta))

    # MULTIPLICACION
    elif operation == "3":
        resultmultiplicacion = (value1 * value2)
        print("El resultado de la multiplicacion es: ", int(resultmultiplicacion))

    # DIVISION
    elif operation == "4":
        resultdivision = (value1 / value2)
        print("El resultado de la division es: ", int(resultdivision))
    else:
        break

    # MENU E INGRESO DE DATOS
    operation = str(input("Ingresar opcion 1.Suma 2.Resta 3.Multiplicacion 4.Division 5.Salir: "))
