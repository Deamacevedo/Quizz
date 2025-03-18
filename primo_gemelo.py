


def es_primo(n):                                                            #Funcion para definir si es primo
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):                                        
        if n % i == 0:
            return False
    return True

def encontrar_dos_primos(inicio, final):                                    #Funcion para encontrar dos primos con rango 2 distancia
    primos_gemelos = []
    for num in range(inicio, final + 1):
        if es_primo(num) and es_primo(num + 2):                             #If para agregar a la lista primos_gemelos si se cumple la condicion
            primos_gemelos.append((num, num + 2))
    return primos_gemelos


def generar_primos_gemelos(inicio,final):                                   #Funcion para imprimir la lista de primos_gemelos
    primos_gemelos = encontrar_dos_primos(inicio, final)                    
    print("Primos gemelos: ",primos_gemelos)                                
    print("")
