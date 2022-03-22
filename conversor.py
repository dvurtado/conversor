menu = """

Welcome to the Platzi Money Converter. 🤑

To continue, please choose among these options:

1. To transform Euros to US dollar
2. To transform Ecuadorian Sucre to US dollar
3. To transform Argentinian Peso to US dollar

"""
option = input(menu)

if option == "1":

    # Conversor de euros a dólares

    euros = input("¿Cuántos euros tienes? ")
    euros = float(euros)
    valor_dolar = 0.90424831
    dolares = euros * valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print ("Tienes $"  + dolares + " dólares")

elif option == "2":

    # conversor de sucres a dólares

    sucre = int (input ("¿Cuántos sucres tienes? "))
    valor_dolar = 25000
    dolar = sucre / valor_dolar
    dolar = round (dolar, 2)
    dolar = str(dolar)
    print ("Tienes $" + dolar + "dólares")


elif option == "3":

    # conversor de pesos a dólares

    pesos = int (input ("¿Cuántos pesos argentinxs tienes? " ))
    valor_dolar = 109.98
    dolar3 = pesos / valor_dolar
    dolar3 = round (dolar3, 2)
    dolar3 = str(dolar3)
    print ("Tienes $" + dolar3 + "dólares")

else: 

    print ("Debe elegir una opción entre 1, 2 y 3")

    


