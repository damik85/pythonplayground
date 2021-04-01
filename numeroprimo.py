# Ingresamos el numero para saber si es primo
num = int(input("Ingrese un numero para saber si es primo: "))

# Valido y calculo si el numero es primo o no
if num > 1:
    for i in range(2, int(num / 2) + 1):
        if (num % i) == 0:
            print(num, "no es un numero primo")
            break
    else:
        print(num, "es un numero primo")
else:
    print(num, "no es un numero primo")
