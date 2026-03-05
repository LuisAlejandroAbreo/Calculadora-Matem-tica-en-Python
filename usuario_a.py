def fibonacci(n):
    serie = []
    a, b = 0, 1
    
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    
    return serie


def serie_fibonacci():
    while True:
        try:
            n = int(input("Ingrese la cantidad de términos: "))
        
            if n <= 0:
                print("Error: Debe ingresar un número entero positivo mayor que 0.")
            else:
                break
            
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    resultado = fibonacci(n)

    print(f"\nLos primeros {n} términos de la serie Fibonacci son:")
    print(resultado)

def num_capicua():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    num_str = str(num)
    if num_str == num_str[::-1]:
        print(f"\nEl número {num} es capicúa.")
    else:
        print(f"\nEl número {num} no es capicúa.")

def num_perfecto():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

    if num < 2:
        print(f"\nEl número {num} no es perfecto.")
        return

    divisores = [i for i in range(1, num) if num % i == 0]
    suma_divisores = sum(divisores)

    if suma_divisores == num:
        print(f"\nEl número {num} es perfecto.")
    else:
        print(f"\nEl número {num} no es perfecto.")
