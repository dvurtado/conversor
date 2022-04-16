# def palindromo(palabra):
#     palabra = palabra.replace(" ", "")
#     palabra = palabra.upper()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return  True
#     else:
#         return False

# def run():
#     palabra = input("Inserte una palabra para analizar")
#     es_palindromo = palindromo(palabra)
#     if es_palindromo == True:
#         print ("Es palindromo")
#     else:
#         print ("No es palindromo")

# if __name__ == "__main__":
#     run()





def palindromo (palabra):
    palabra = palabra.replace(" ", "")
    palabra = palabra.upper()
    reves = palabra[::-1]
    if palabra == reves:
        return True
    else:
        return False



def run ():
    palabra = input("Inserte una palabra: ")
    es_palindromo = palindromo (palabra)
    if es_palindromo == True:
        print("Es palíndromo")
    else:
        print ("No es palíndromo")




if __name__ == "__main__":
    run()
    







