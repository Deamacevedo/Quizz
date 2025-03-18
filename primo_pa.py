import math

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def es_palindromico(n):
    return str(n) == str(n)[::-1]

def encontrar_primos_palindromicos(inicio, final):
    primos_palindromicos = []
    for num in range(inicio, final + 1):
        if es_primo(num) and es_palindromico(num):
            primos_palindromicos.append(num)
    return primos_palindromicos

inicio = 1
final = 1000
def generar_numeros_palindromicos(inicio,final):
    primos_palindromicos = encontrar_primos_palindromicos(inicio, final)
    print(primos_palindromicos)
