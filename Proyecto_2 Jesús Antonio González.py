#Programa para identificar la longitud de una palabra ingresada.(La longitud tiene que ser entre 4 y 8 letras.)
palabra = input("Ingrese una palabra: ")
longitud = len(palabra)
#Si la palabra es menor de 4 letras se imprime "Hacen falta letras."
if longitud < 4:
    print (f"Hacen falta letras. Solo tiene {longitud} letras.")
#Si la palabra que se proporciona tiene entren 4 y 8 letras. Se imprime que la palabra es correcta.
elif 4<= longitud <=8 :
    print("La longitud proprocionada es la adecuada. La palabra es correcta. ")
else:
    print ( f"Sobran letras.Tiene {longitud} letras.")
    

#################################################################################################

#Programa para encontrar el cuadrante de acuerdo a las coordenadas X o Y proporcionadas.     
def encontrar_cuadrante (x, y) :
#Si la coordenada X o Y es son mayor a cero, se encontrara en el cuadrante I.   
    if x > 0 and y > 0:
        return "Cudrante I"
# Si la coordenada X es menor a 0, y la coordenada Y mayor a cero se encontrara en cuadrante 2.
    elif x < 0 and y > 0:
        return "Cuadrante II"
# Si ambas coordenadas X,Y son menor a cero, se encontrara en el cuadrante 3.
    elif x < 0 and y <0 :
        return "Cuadrante III"
#Si la coordenada X es mayor a 0 y la coordenada Y es menor a 0, se encontrara en el cuadrante 4.
    elif x > 0 and y < 0:
        return "Cuadrante IV"
    elif x == 0 and y != 0:
        return"Sobre el eje Y"
    elif y == 0 and x !=0:
        return "Sobre el eje X"
    else:
        return "Origen"
    
x = int(input("Ingrese la coordenada X: "))
y = int(input("Ingrese la coordenada Y: "))
cuadrante = encontrar_cuadrante (x,y)
print(f"La coordenada ({x} , {y}) se encuentra en {cuadrante}.")


