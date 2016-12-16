#Pida al usuario una lista de numeros enteros y que muestre en la pantalla el mayor numero impar
#Katya Jared Amador Rodriguez
#13/12/16
a = input ("Ingrese una lista: ")
elemento=a[0:]
lista=[]
for elemento in a:
    if(elemento%2==0):
        f=[elemento]
#        print(str(elemento)+" es par")
    else:
            g=[elemento]
            lista.append(g)
            lista.sort()
print "El numero impar mayor ingresado es: ",lista[-1]
