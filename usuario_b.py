def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def numeros_primos():
    inicio = int(input("  Valor inicial: "))
    fin = int(input("  Valor final:   "))

    primos = [n for n in range(inicio, fin + 1) if es_primo(n)]

    print(f"\n  Primos entre {inicio} y {fin}:")
    print(f"  {primos}")
    print(f"  Total: {len(primos)} números primos")
    print("----------------------------------")

def verificar_primo():

    print("\n--- Verificar si un Número es Primo ---")
    n = int(input("  Ingresa un número: "))

    if es_primo(n):
        print(f"\n {n} ES un número primo.")
    else:
        print(f"\n {n} NO es un número primo.")
    print("---------------------------------------")

def factorial():
    pass


def maximo_comun_divisor():
    pass
