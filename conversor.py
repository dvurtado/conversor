from threading import local


def conversor (moneda_local, tipo_cambio):

    local = input("Ingrese la cantidad de" + moneda_local + "que dispone")
    local = float(local)
    dolares = local / tipo_cambio
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("Usted tiene " + dolares + "en su cuenta bancaria :")

menu = """
Bienvenido al menu de opciones del conversor internacional de monedas:

1. De pesos argentinos a dólares.
2. De sucres a dólares
3. De pesos colombianos a dólares

"""

opcion = int(input (menu) )

if opcion == 1:
    conversor ("pesos argentinos", 109)

elif opcion ==2:
    conversor ("pesos colombianos", 3750)

elif opcion == 3:
    conversor ("sucres ecuatorianos", 25000)

else:
    print("Escoja una opción viable")



