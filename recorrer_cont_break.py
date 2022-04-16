def run ():
    
    # for contador in range(1000+1):
    #     if contador % 2 != 0:
    #         continue
    #     else:
    #         print (contador)


    # for contador in range (20000):
    #     print (contador)
    #     if contador == 7520:
    #         break

    

    i = input("Inserte una palabra: ")
    for letra in i:
        if letra == "o":
            break
        print (letra)


    # And now I'll be using "While"

    # i = int(input("Inserte un número: "))
    # while i <= 1000:
    #     if i == 563:
    #         break
    #     print (i)
    #     i+=1
    
    texto = input("Escribe un texto: ")
    for letra in texto: 
        if letra == "o":
            break
    print(letra)



if __name__ == "__main__":
    run()