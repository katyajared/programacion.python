#Pida al ususario una palabra y devuelva la palabra escrita en orden inverso
#Katya Jared Amador Rodriguez
#13/12/16
palabra=input("Ingrese una palabra entre comillas: ")
print palabra
a=0
inverso=""
b=len(palabra)-1
while (a<=b):
    inverso=inverso+palabra[b]
    b=b-1
print "Su palabra escrita en orden inverso es: ", inverso
