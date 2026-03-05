from usuario_a import serie_fibonacci, num_capicua, num_perfecto
from usuario_b import calcular_factorial, verificar_primo, maximo_comun_divisor, numeros_primos 

def menu():
    print("""\n*** CALCULADORA MATEMÁTICA *** \n
1. SERIE FIBONACCI
2. NUMERO CAPICUA
3. NUMERO PERFECTO
4. NUMEROS PRIMOS
5. VERIFICAR SI UN NUMERO ES PRIMO
6. CALCULAR FACTORIAL
7. MAXIMO COMUN DIVISOR
8. SALIR""")

def main():
    
    while(True):
        menu()
        op = input("Opcion? ").strip()

        if op =="1":
            serie_fibonacci()
        elif op =="2":
            num_capicua()
        elif op =="3":
            num_perfecto()
        elif op =="4":
            numeros_primos()
        elif op =="5":
            verificar_primo()
        elif op =="6":
            calcular_factorial()
        elif op =="7":
            maximo_comun_divisor()
        elif op =="8":
            print("Gracias por usar el programa")
            break
        else:
            print("Error. Opcion invalida")
        input ("Digite cualquier letra para continuar")

main()
