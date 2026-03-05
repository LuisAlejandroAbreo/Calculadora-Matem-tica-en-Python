def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def numeros_primos(inicio, fin):
    for n in range(inicio, fin + 1):
        if es_primo(n):
         return n

def verificar_primo():
    pass

def factorial():
    pass


def maximo_comun_divisor():
    pass

