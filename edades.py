edad = int ( input ("Digite su edad: ")  )
if edad >= 18 and edad < 65:
    print ("Usted es mayor de edad")

elif edad >= 65:
    print ("Usted es de la tercera edad")

elif edad >= 0 and edad <= 5:
    print ("Ciudadano perteneciente a la primera infancia")

else:
    print ("Usted es menor de edad")