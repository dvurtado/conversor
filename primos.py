

def es_primo(numero):
    contador = 0
    for i in range (1, numero +1 ):
        if numero % i == 0: 
            contador += 1
    if contador == 2:
        return True

    else:
        return False 


        
def run ():
    numero = int(input("Escribe un número: "))
    if es_primo(numero) == True:
        print("Es número primo")
    else:
        print("No es primo")       



if __name__ == "__main__":
    run()

