#Pedir datos al usuario
Nombre = input ("Introduce tu Nombre: ")
Apellido_paterno= input ("Introduce tu apellido paterno: ")
Apellido_materno = input ("Introduce tu apellido materno: ")
cond = False
while cond == False:
    try:
        Edad = float(input("Introduce tu edad: "))
        if Edad <0:
            print("Por favor introduce un numero valido")
        else: 
            cond = True     
    except ValueError:   
        print("Por favor ingrese un numero valido")
print(f"{Nombre} tiene {Edad} años ")

def calcular_IMC (Estatura, Peso):
    return Peso / Estatura**2
Peso = float (input("Introduce tu peso en Kg: "))
        
Estatura = float (input("Introduce tu estarura en " + "Metros: "))

IMC = calcular_IMC (Estatura, Peso)
print("{:.2f}" .format(IMC))


