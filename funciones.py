def conversor (moneda_local, tipo_cambio):
    a = input ("Ingrese su " + moneda_local + " por favor: ") 
    a = float(a)
    dolares = a / tipo_cambio
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print ("Usted tiene una cantidad de: " + dolares + " en su cuenta bancaria")

menu = """

    Bienvenido al conversor de monedas, donde todo lo convertimos rápido. 

    1. De pesos argentinos a dólares
    2. De sucres a dólares
    3. De COP a dólares

"""

opcion = int( input(menu))

if opcion == 1:
    conversor ("pesos argentinos", 900)

elif opcion ==2:
    conversor ("sucres", 25000)

elif opcion == 3:
    conversor ("COP", 2780)

else:
    print("Selecciona una opción correcta")



