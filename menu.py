from primo_gemelo import generar_primos_gemelos
from primo_pa import generar_numeros_palindromicos

def menu():
            print("******************************")
            print("********NUMEROS PRIMOS********")
            print("******************************")
            print("Digite la opcion a realizar")
            print("1.Encontrar numeros primos gemelos.")
            print("2.Encontrar numeros primos palindromicos.")
            print("3.Salir del programa")
            print()

def mostrar_menu ():    

    while True:
        menu()
        opc = input()
        match opc:
            case "1":
                try:
                    limite = input("Ingrese el limite superior: ")
                    limite_ent = int(limite)
                    generar_primos_gemelos(2,limite_ent)
                    print("")
                except Exception:
                    print("Digite un numero entero valido como limite superior")
                    print("")
            case "2":
                try:
                    limite = input("Ingrese el limite superior: ")
                    limite_ent = int(limite)
                    generar_numeros_palindromicos(10,limite_ent)
                    print("")
                except Exception:
                    print("Digite un numero entero valido como limite superior")
                    print("")
            case "3":              
                print("*********************")  
                print("Saliendo del programa")
                print("*********************")
                print("")
                break
            case _:
                print("Digite una opcion correcta de las anteriormente mencionadas")
                print("")