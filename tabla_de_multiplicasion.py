print(" ")
print("Alexa guadalupe Ramirez Manzo 1205 3-W")
print(" ")
numero = int(input("Introduce un número para mostrar su tabla de multiplicar: ")) #variable para la tabla de multiplicar
#rngo de 1 al 10
for i in range(1, 11):  # Desde 1 hasta 10 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

