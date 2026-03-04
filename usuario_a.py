def fibonacci(n):
    serie = []
    a, b = 0, 1
    
    for _ in range(n):
        serie.append(a)
        a, b = b, a + b
    
    return serie

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

