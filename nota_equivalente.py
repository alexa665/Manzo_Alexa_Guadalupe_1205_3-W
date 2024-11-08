print(" ")
print("Alexa Guadalupe Ramirez Manzo 1205 3-W")
print(" ")
calificasion = float(input("Introduce la calificasion: ")) #variable, y preguntamos la calificasion con desimales
print(" ")
#comparamos las calificasiones utilisando if, else y pusimos el mensaje pedido
if 0 <= calificasion < 5:
    print("SUSPENSO")
elif 5 <= calificasion < 6:
    print("SUFICIENTE")
elif 6 <= calificasion < 7:
    print("BIEN")
elif 7 <= calificasion < 9:
    print("NOTABLE")
elif 9 <= calificasion <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")




